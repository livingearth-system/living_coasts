import numpy as np
import xarray as xr

import datacube
dc = datacube.Datacube()


def vegetation_loss(query_pre_impact, query_post_impact):
    '''
    Vegetation loss (extent)
    TODO: put in defintion here

    # Level 3
    Cultivated terrestrial vegetation (111) --> Bare surface (216)
    Natural terrestrial vegetation (112) --> Bare surface (216)
    Natural aquatic vegetation (124) --> Bare surface (216) 

    Cultivated terrestrial vegetation (111) --> Water (220)
    Natural terrestrial vegetation (112) --> Water (220)
    Natural aquatic vegetation (124) --> Water (220)

    Cultivated terrestrial vegetation (111) --> Artificial surfaces (215)
    Natural terrestrial vegetation (112) --> Artificial surfaces (215)
    Natural aquatic vegetation (124) --> Artificial surfaces (215)
    '''
    # load in Land cover for time periods
    L3_pre_impact_year = dc.load(
        product="ga_ls_landcover_class_cyear_2",
        output_crs="EPSG:3577",
        measurements=["level3"],
        **query_pre_impact)

    L3_post_impact_year = dc.load(
        product="ga_ls_landcover_class_cyear_2",
        output_crs="EPSG:3577",
        measurements=["level3"],
        **query_post_impact)

    # combine years to one xr.dataarray
    combined = xr.concat([L3_pre_impact_year, L3_post_impact_year], dim="time")
    combined_da = combined.level3

    # create where statements
    # output raster as vegetation loss (1 or np.nan)
    vegetation_loss = xr.where((combined_da[0] == 111) & (combined_da[1] == 215) |
                               (combined_da[0] == 112) & (combined_da[1] == 215) | 
                               (combined_da[0] == 124) & (combined_da[1] == 215) | 
                               (combined_da[0] == 111) & (combined_da[1] == 216) | 
                               (combined_da[0] == 112) & (combined_da[1] == 216) | 
                               (combined_da[0] == 124) & (combined_da[1] == 216) | 
                               (combined_da[0] == 111) & (combined_da[1] == 220) | 
                               (combined_da[0] == 112) & (combined_da[1] == 220) | 
                               (combined_da[0] == 124) & (combined_da[1] == 220), 1, np.nan)

    return vegetation_loss



def vegetation_damage(query_pre_impact, query_post_impact):
    '''
    Vegetation damage (strong winds)
    Definition: Harm that impairs the value or function of plants or plant communities.

    # Level 3
    Cultivated terrestrial vegetation (111) --> Cultivated terrestrial vegetation (111)
    Natural terrestrial vegetation (112) --> Natural terrestrial vegetation (112)
    Natural aquatic vegetation (124) --> Natural aquatic vegetation (124)
    
    # Level 4
    Vegetation Cover (Canopyco_veg_cat14d)
    Closed >65% (10) --> Open 40% - 65% (12) OR Open 15% to 40% (13) OR Sparse (4% to 15%) OR Scattered 1 to 4% (16)
    Open 40% - 65% (12) --> Open 15% to 40% (13) OR Sparse (4% to 15%) OR Scattered 1 to 4%
    Open 15% to 40% (13) --> Sparse (4% to 15%) OR Scattered 1 to 4%
    Sparse (4% to 15%) --> Scattered 1 to 4% (16)
    '''
    # Load in Land cover for time periods
    pre_impact_year = dc.load(
        product="ga_ls_landcover_class_cyear_2",
        output_crs="EPSG:3577",
        measurements=["level3", "vegetation_cover"],
        **query_pre_impact)

    post_impact_year = dc.load(
        product="ga_ls_landcover_class_cyear_2",
        output_crs="EPSG:3577",
        measurements=["level3", "vegetation_cover"],
        **query_post_impact)

    # Combine years into one xr.Dataset
    combined = xr.concat([pre_impact_year, post_impact_year], dim="time")
    combined_level3 = combined.level3
    combined_vegetation_cover = combined.vegetation_cover

    # Create where statements for vegetation damage
    condition_1 = (combined_level3[0] == 111) & (combined_level3[1] == 111) & \
                  (combined_vegetation_cover[0] == 10) & \
                  ((combined_vegetation_cover[1] == 12) | 
                   (combined_vegetation_cover[1] == 13) | 
                   (combined_vegetation_cover[1] == 16))

    condition_2 = (combined_level3[0] == 112) & (combined_level3[1] == 112) & \
                  (combined_vegetation_cover[0] == 10) & \
                  ((combined_vegetation_cover[1] == 12) | 
                   (combined_vegetation_cover[1] == 13) | 
                   (combined_vegetation_cover[1] == 16))

    condition_3 = (combined_level3[0] == 124) & (combined_level3[1] == 124) & \
                  (combined_vegetation_cover[0] == 10) & \
                  ((combined_vegetation_cover[1] == 12) | 
                   (combined_vegetation_cover[1] == 13) | 
                   (combined_vegetation_cover[1] == 16))

    vegetation_damage = xr.where(condition_1 | condition_2 | condition_3, 1, np.nan)

    return vegetation_damage
