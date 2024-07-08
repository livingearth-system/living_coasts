from datacube.virtual import Transformation, Measurement
from datacube.utils import masking
from dea_tools.datahandling import wofs_fuser

import datacube
dc = datacube.Datacube()

class fractional_cover(Transformation):

    def compute(self, data):
        return data     
        
        # Drop invalid data
        data = masking.mask_invalid_data(data)
        
        # Load DEA Water Observations data from the datacube
        wo = dc.load(
            product='ga_ls_wo_3',
            group_by='solar_day',
            fuse_func=wofs_fuser,
            like=data)

        # Mask dry, non-cloudy pixels
        wo_mask = masking.make_mask(wo.water, dry=True)
        
        # Apply the mask to fractional cover data
        fc_masked = data.where(wo_mask)
        
        return fc_masked


    def measurements(self, input_measurements):
        return {'data': Measurement(name='fractional_cover', dtype='float32', nodata=float('nan'), units='1')}
