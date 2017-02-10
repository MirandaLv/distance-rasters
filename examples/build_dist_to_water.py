
import sys
import os
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base)

from main import build_distance_array
from utils import rasterize, export_raster


# -----------------------------------------------------------------------------

from affine import Affine
# import numpy as np

shorelines_path = "/sciclone/aiddata10/REU/raw/shorelines/GSHHS_f_L1_lines.shp"

lakes_path = "/sciclone/aiddata10/REU/raw/natural_earth/ne_10m_lakes/ne_10m_lakes.shp"

rivers_path = "/sciclone/aiddata10/REU/raw/natural_earth/ne_10m_rivers_lake_centerlines/ne_10m_rivers_lake_centerlines.shp"

pixel_size = 0.01

xmin = -180
xmax = 180
ymin = -90
ymax = 90

affine = Affine(pixel_size, 0, xmin,
                0, -pixel_size, ymax)


shape = (int((ymax-ymin)/pixel_size), int((xmax-xmin)/pixel_size))

shorelines, _ = rasterize(path=shorelines_path, affine=affine, shape=shape)
lakes, _ = rasterize(path=lakes_path, affine=affine, shape=shape)
rivers, _ = rasterize(path=rivers_path, affine=affine, shape=shape)


water = shorelines + lakes + rivers


water_output_raster_path = "/sciclone/aiddata10/REU/data/rasters/external/global/distance_to/water/water_binary.tif"

export_raster(water, affine, water_output_raster_path)


# -----------------------------------------------------------------------------

# import rasterio
# water_src = rasterio.open(water_output_raster_path)
# water = water_src.read()[0]
# affine = water_src.affine

distance_output_raster_path = "/sciclone/aiddata10/REU/data/rasters/external/global/distance_to/water/water_distance.tif"


def raster_conditional(rarray):
    return (rarray == 1)

dist = build_distance_array(water, affine=affine,
                            output=distance_output_raster_path,
                            conditional=raster_conditional)


