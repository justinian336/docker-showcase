from pathlib import Path
import json
import numpy as np
from shapely.geometry import Polygon, MultiPolygon
import h3
import rasterio
from rasterio.mask import mask
import geopandas as gpd

base = Path('/home/rstudio/data_processing')

def pref_to_shape(res):
    # Read the night light data (DMSP-OLS sensor data for satellite F16, year 2017. Just one pass.)
    nightlight = rasterio.open(base/'night_lights'/'F16201701041855.night.OIS.vis.co.tif')
    # Read the file (use `sf` and  `jpndistricts` in R to obtain the FeatureCollection)
    with open(base/'geojson'/'south_kanto.geojson', 'r') as f:
        tokyo = json.load(f)
        
    # Store here all the hexagons within the prefecture
    hexagons = set([])
    for f in tokyo['features']:
        for i in f['geometry']['coordinates']:
            for j in i:
                poly = Polygon(j)
                hexagons.update(h3.polyfill_geojson(poly.__geo_interface__, res))
                
    # zip the hexagons and their shapes
    hexagons = list(hexagons)
    polys = [Polygon(h3.h3_to_geo_boundary(hexagon, geo_json=True)) for hexagon in hexagons]
    # Store here the mean lights values:
    mean_lights = []
    
    for poly in polys:
        # Mask the raster with the hexagon
        masked_light = mask(nightlight, MultiPolygon([poly]), crop=True, nodata=255)
        # Obtain the mean light value for the hexagon (exclude nulls)
        mean_light = np.mean(masked_light[0][masked_light[0] != 255])
        mean_lights.append(mean_light)
    
    df = gpd.GeoDataFrame({'mean_light': mean_lights}, geometry=polys)
    df.to_file(base/'output/south_kanto_lights.shp')

pref_to_shape(7)
