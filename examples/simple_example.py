
import sys
import os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base)


from main import build_distance_array
from utils import rasterize, export_raster

# -----------------------------------------------------------------------------

shp_path = "{0}/data/line_test/line_test.shp".format(base)
out_name = "line_test"

# shp_path = "data/line_test/big_line.shp"
# out_name = "big_line"

# shp_path = "data/ca_riv_15s/ca_riv_15s.shp"
# out_name = "ca_riv_15s"

# -----------------------------------------------------------------------------

pixel_size = 0.01

rasterized_features_path = "{0}/data/{1}_binary_raster.tif".format(base, out_name)


rv_array, affine = rasterize(path=shp_path, pixel_size=pixel_size,
                             output=rasterized_features_path)

# export_raster(rv_array, affine, rasterized_features_path)


# print rv_array
print rv_array.shape
print affine

# -----------------------------------------------------------------------------

distance_raster_path = "{0}/data/{1}_distance_raster.tif".format(base, out_name)

def raster_conditional(rarray):
    return (rarray == 1)

build_distance_array(rv_array, affine=affine,
                     output=distance_raster_path,
                     conditional=raster_conditional)


