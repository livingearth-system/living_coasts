import datacube
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas as pd
import xarray as xr
import odc.geo.xr
#import rasterio
import geopandas as gpd # Added from WDC

from odc.algo import xr_reproject # From https://docs.dea.ga.gov.au/notebooks/How_to_guides/Reprojecting_data.html

import sys, os
sys.path.insert(1, os.path.abspath('../Tools'))
from dea_tools.plotting import rgb, display_map
from dea_tools.datahandling import wofs_fuser  # Added from DEA plotting
from dea_tools.plotting import rgb, plot_wo  # Added from DEA plotting
from matplotlib import colors as mcolours
from dea_tools.landcover import plot_land_cover, lc_colourmap, make_colorbar
from datacube.testutils.io import rio_slurp_xarray
from datacube.utils import masking # Added from DEA plotting
from datacube.utils.masking import mask_invalid_data
#from datacube.utils import cog  # Temporarily disabled
from datacube.utils.cog import write_cog
# from display_tools import map_geom, rgb # from WDC - not accessing
from ipyleaflet import GeoData # Added from WDC 
from time import time as time # Added from burn notebook
import datetime as dt # Added from burn notebook
from odc.geo.geom import Geometry
from dea_tools.plotting import rgb

from matplotlib.colors import ListedColormap # Added from WDC
import matplotlib.colors as colors # Added from WDC
from matplotlib import colormaps
import matplotlib.pyplot as plt # Added from WDC
from matplotlib.patches import Patch # Added from WDC

from time import time as time # Added from WDC
import warnings # Added from WDC
warnings.filterwarnings("ignore") # Added from WDC

from landcover import plot_land_cover, lc_colourmap, make_colorbar #added from DEA

#For DEA burn mapping
from datetime import datetime
from datetime import timedelta

from dea_tools.datahandling import load_ard
from dea_tools.plotting import rgb, display_map
from dea_tools.bandindices import calculate_indices
from dea_tools.dask import create_local_dask_cluster
import display_tools as display_tools

# Create local dask cluster to improve data load time
client = create_local_dask_cluster(return_client=True)

from ipyleaflet import DrawControl, FullScreenControl, LayersControl, Map, Rectangle, WidgetControl, basemaps # Added rectangle RML
from ipywidgets import Button, Dropdown, FloatText, GridspecLayout, Layout, HBox, VBox, Output, Tab, interact, widgets

# Additional libraries etc.

from datacube.utils.geometry import Geometry, CRS
from ipyleaflet import GeoData
from display_tools import map_geom, rgb

sys.path.append("../Tools/wdc_tools")
from wdc_datahandling import geopolygon_masking
