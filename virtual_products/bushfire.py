from datacube.virtual import Transformation, Measurement
from datacube.utils import masking
from dea_tools.bandindices import calculate_indices

import datacube
dc = datacube.Datacube()

class bushfire(Transformation):

    def compute(self, data):
        # generate NBR
        data = calculate_indices(baseline,
                             index='NBR',
                             collection='ga_ls_3',
                             drop=False)
        
        return data


    def measurements(self, input_measurements):
        return {'data': Measurement(name='NBR', dtype='float32', nodata=float('nan'), units='1')}
