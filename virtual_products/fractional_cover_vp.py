from datacube.virtual import Transformation, Measurement
from datacube.utils import masking
import datacube
import matplotlib.pyplot as plt
import sys

# Importing custom DEA tools
sys.path.append("/home/jovyan/code/dea-notebooks/Tools")
from dea_tools.datahandling import wofs_fuser
from dea_tools.plotting import rgb, plot_wo, display_map

class FractionalCoverTransformation(Transformation):
    
    def __init__(self, **settings):
        pass

    def compute(self, data):
        # Drop invalid data
        data = masking.mask_invalid_data(data)
        
        # Load DEA Water Observations data from the datacube
        dc = datacube.Datacube(app='DEA_Fractional_Cover')
        wo = dc.load(
            product='ga_ls_wo_3',
            group_by='solar_day',
            fuse_func=wofs_fuser,
            like=data  
        )

        # Mask dry, non-cloudy pixels
        wo_mask = masking.make_mask(wo.water, dry=True)
        
        # Apply the mask to fractional cover data
        fc_masked = data.where(wo_mask)
        
        return fc_masked

    def measurements(self, input_measurements):
        return {
            'bs': Measurement(name='bs', dtype='float32', nodata=float('nan'), units='1'),
            'pv': Measurement(name='pv', dtype='float32', nodata=float('nan'), units='1'),
            'npv': Measurement(name='npv', dtype='float32', nodata=float('nan'), units='1')
        }
