# # wdc_datahandling.py

'''
Description: This file contains a set of python functions for handling
satellite data.
License: The code in this notebook is licensed under the Apache License,
Version 2.0 (https://www.apache.org/licenses/LICENSE-2.0). Aberystwyth
University data is licensed under the Creative Commons by Attribution 4.0
license (https://creativecommons.org/licenses/by/4.0/).
Contact: If you need assistance, please contact Richard Lucas or
Carole Planque from Aberystwyth University.
'''


def export_to_GeoTiff(xarray, bandname=None, filename=None):
    if filename is None:
        raise Exception(f'Filename is missing! You must specify a filename to export your xarray.')
    if bandname is not None:
        xarray = xarray.to_dataset(name=bandname)
        xarray.rio.to_raster(filename)
    else:
        xarray.rio.to_raster(filename)
    print("Array exported to "+filename) 


def cleaning_s2(ds):
    """
    Takes Sentinel-2 dataset and returns a clean dataset (i.e., cloud masked and normalized reflectance).  
    
    Parameters
    ----------
    ds : xarray.Dataset with scl (i.e., cloud mask) variable.
    """    
    print("Cleaning Sentinel-2 images...")
    ds_clean = ds.where((ds.scl == 4) | (ds.scl == 5) | 
                        (ds.scl == 6) | (ds.scl == 7) | 
                        (ds.scl == 11))
    ds_clean = ds_clean.where(ds_clean != 0)
    ds_clean = ds_clean.drop('scl')
    
    # Add negative BOA offset for Sentinel-2 L2A images produced from the 04.00 baseline (i.e., since 25 January 2022)
    # L2A_BOAi = (L2A_DNi + BOA_ADD_OFFSETi) / QUANTIFICATION_VALUEi
    
    print("(Applying new Copernicus offset after 24 Jan 2022.)")
    ds_clean_withOFFSET = ds_clean.where(ds_clean.time.dt.year > 2022) - 1000
    
    ds_clean_withOFFSET_2022 = ds_clean.where((ds_clean.time.dt.month > 1) & (
                                               ds_clean.time.dt.year == 2022)) - 1000
    
    ds_clean_withOFFSET_Jan2022 = ds_clean.where((ds_clean.time.dt.day >= 25) & (
                                                  ds_clean.time.dt.month == 1) & (
                                                  ds_clean.time.dt.year == 2022)) - 1000
    
    ds_clean_withoutOFFSET_Jan2022 = ds_clean.where((ds_clean.time.dt.day < 25) & (
                                                     ds_clean.time.dt.month == 1) & (
                                                     ds_clean.time.dt.year == 2022))
    
    ds_clean_withoutOFFSET = ds_clean.where(ds_clean.time.dt.year < 2022)
    
    ds_clean_addedOFFSET = ds_clean_withoutOFFSET.fillna(0) + ds_clean_withoutOFFSET_Jan2022.fillna(0
                         ) + ds_clean_withOFFSET_Jan2022.fillna(0) + ds_clean_withOFFSET_2022.fillna(0
                         ) + ds_clean_withOFFSET.fillna(0)
    
    return (ds_clean_addedOFFSET/10000)

def cloud_coverage(ds):
    """
    Takes EO dataset and returns the non-valid coverage (%).  
    
    Parameters
    ----------
    ds : xarray.Dataset
    """
    Clouds = ds[list(ds.keys())[0]].fillna(1).where(
        (9999 - ds[list(ds.keys())[0]].fillna(0))==9999)
    
    if (('longitude' in ds.dims) & ('latitude' in ds.dims)):
        area_total_size = len(ds.longitude)*len(ds.latitude)
        cloud_percentage = Clouds.count(['latitude','longitude'])/area_total_size *100
        
    elif (('x' in ds.dims) & ('y' in ds.dims)):
        area_total_size = len(ds.x)*len(ds.y)
        cloud_percentage = Clouds.count(['y','x'])/area_total_size *100
    else:
        raise Exception(
                f'Dimensions not recognised; please provide a xarray.Dataset '
                'with longitude/latitude or x/y dimensions.')
    
    return cloud_percentage


def geom_fromextent(site):
    from datacube.utils.geometry import Geometry, CRS
    from shapely.geometry.polygon import Polygon
    
    coords = [(site[0], site[1]), (site[0], site[3]), (site[2], site[3]), [site[2], site[1]], (site[0], site[1])]
    geom_extent=Geometry(geom=Polygon(coords), crs=CRS("epsg:4326"))
    return geom_extent


def geom_fromdrawn(option='Extent', shapefile=None):
    import display_tools
    from datacube.utils.geometry import Geometry, CRS
    from shapely.geometry.polygon import Polygon
    
    try:
        geojson = display_tools.DRAW_GEOJSON_GEOM
    except:
        raise Exception(
                f'NO GEOMETRY RETURNED; Please draw a polygon first and then re-run this cell.')
    
    if (shapefile is not None):
        shapefile = shapefile.to_crs(epsg=4326)
    if option == 'Extent':
        geom_extent = Geometry(geom=geojson, crs=CRS("epsg:4326"))
        id_shapefile = None
    if option == 'Selection':
        if (shapefile is None):
            raise Exception(
                f'"Selection" option was provided; please provide a GeoDataFrame '
                'to select data from')
        geom = Polygon([tuple(l) for l in geojson['coordinates'][0]])
        selected_field = shapefile.loc[shapefile.index == shapefile.contains(geom)[
                                         shapefile.contains(geom)].index[0]]
        geom_extent = Geometry(geom= selected_field.geometry[selected_field.index[0]], crs=CRS("epsg:4326"))
        id_shapefile = selected_field.id.values
    
    return geom_extent, id_shapefile



def geopolygon_masking(ds, geopolygon):
    from shapely.geometry import shape
    import geopandas as gpd
    import rasterio
    import xarray as xr
    gpd_geom = [shape(geopolygon)]
    gpd_feature = gpd.GeoDataFrame({'geometry':gpd_geom}).set_crs(geopolygon.crs).to_crs(ds.rio.crs)
    
    if ('latitude' in ds.dims) and ('longitude' in ds.dims):
        ShapeMask = rasterio.features.geometry_mask(gpd_feature.iloc[0],
                                              out_shape=(len(ds.latitude), len(ds.longitude)),
                                              transform=ds.geobox.transform,
                                              invert=True)
        ShapeMask = xr.DataArray(ShapeMask , dims=("latitude", "longitude"))
    elif ('y' in ds.dims) and ('x' in ds.dims):
        ShapeMask = rasterio.features.geometry_mask(gpd_feature.iloc[0],
                                              out_shape=(len(ds.y), len(ds.x)),
                                              transform=ds.geobox.transform,
                                              invert=True)
        ShapeMask = xr.DataArray(ShapeMask , dims=("y", "x"))
    else:
        raise Exception(
                f'Dimensions not recognised; please provide a xarray.Dataset '
                'with longitude/latitude or x/y dimensions.')
    
    masked_dataset = ds.where(ShapeMask == True)
    return masked_dataset
