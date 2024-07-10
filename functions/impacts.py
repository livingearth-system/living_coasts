import numpy as np
import xarray as xr

import datacube
dc = datacube.Datacube()


def vegetation_loss(query_pre_impact, query_post_impact):
    '''
    Vegetation loss (extent)
    TODO: put defintion here

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
