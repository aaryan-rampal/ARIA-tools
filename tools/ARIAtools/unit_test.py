# import pickle

# from ARIAtools.ARIA_global_variables import ARIA_EXTERNAL_CORRECTIONS, \
#     ARIA_TROPO_MODELS, ARIA_STACK_DEFAULTS, ARIA_STACK_OUTFILES
# import os
# import glob
# import logging
# import argparse
# import multiprocessing
# from collections import defaultdict
# from datetime import datetime
# from osgeo import gdal

# # Import functions
# from ARIAtools import progBar
# from ARIAtools.ARIAProduct import ARIA_standardproduct
# from ARIAtools.mask_util import prep_mask
# from ARIAtools.shapefile_util import open_shapefile
# from ARIAtools.vrtmanager import resampleRaster, layerCheck, \
#     get_basic_attrs, dim_check
# from ARIAtools.extractProduct import merged_productbbox, prep_dem, \
#     export_products, gacos_correction

# gdal.UseExceptions()
# # Suppress warnings
# gdal.PushErrorHandler('CPLQuietErrorHandler')

# log = logging.getLogger(__name__)

# # Import the function you want to debug
# from ARIAtools.extractProduct import merged_productbbox, prep_dem, \
#     export_products, gacos_correction

# # Load the saved objects
# with open('saved_objects.pkl', 'rb') as f:
#     standardproduct_info, layers, rankedResampling, export_dict = pickle.load(f)

# demfile = gdal.Open('saved_gdal_dataset.tif')

# export_dict['dem'] = demfile

# # Call the function with the loaded objects
# ref_arr_record = export_products(standardproduct_info.products[1],
#                                  tropo_total=False,
#                                  layers=layers,
#                                  rankedResampling=rankedResampling,
#                                  **export_dict)

import pickle

from ARIAtools.ARIA_global_variables import ARIA_EXTERNAL_CORRECTIONS, \
    ARIA_TROPO_MODELS, ARIA_STACK_DEFAULTS, ARIA_STACK_OUTFILES
import os
import glob
import logging
import argparse
import multiprocessing
from collections import defaultdict
from datetime import datetime
from osgeo import gdal

# Import functions
from ARIAtools import progBar
from ARIAtools.ARIAProduct import ARIA_standardproduct
from ARIAtools.mask_util import prep_mask
from ARIAtools.shapefile_util import open_shapefile
from ARIAtools.vrtmanager import resampleRaster, layerCheck, \
    get_basic_attrs, dim_check
from ARIAtools.extractProduct import merged_productbbox, prep_dem, \
    export_products, gacos_correction

gdal.UseExceptions()
# Suppress warnings
gdal.PushErrorHandler('CPLQuietErrorHandler')

log = logging.getLogger(__name__)

# Import the function you want to debug
from ARIAtools.extractProduct import merged_productbbox, prep_dem, \
    export_products, gacos_correction

# Load the saved objects
with open('saved_objects.pkl', 'rb') as f:
    a, layers, export_dict = pickle.load(f)

demfile = gdal.Open('saved_gdal_dataset.tif')

export_dict['dem'] = demfile

import pdb
# Call the function with the loaded objects
ref_arr_record = export_products(a,
                                 tropo_total=False,
                                 layers=layers,
                                 **export_dict)
print(ref_arr_record)
