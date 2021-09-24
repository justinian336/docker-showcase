FROM rocker/geospatial:4

COPY ./ /home/rstudio

WORKDIR /home/rstudio

RUN apt-get update && apt-get install -y python3-dev python3-pip && \
    pip3 install awscli geopandas shapely rasterio h3 && \
    mkdir ./data_processing/night_lights ./data_processing/geojson ./data_processing/output

RUN Rscript -e "devtools::install_github('uribo/jpndistrict')"

RUN aws s3 cp s3://globalnightlight/F162017/F16201701041855.night.OIS.vis.co.tif \
/home/rstudio/data_processing/night_lights/ --no-sign-request

RUN Rscript ./data_processing/get_south_kanto_geojson.R

RUN python3 ./data_processing/tile_aggregation.py
