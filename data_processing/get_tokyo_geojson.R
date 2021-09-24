library(jpndistrict)
south_kanto_geometry <- jpndistrict::jpn_cities(c('11', '12', '13', '14'))
south_kanto_geometry <- south_kanto_geometry[
    (stringr::str_sub(south_kanto_geometry$city_code, end=2) != '13') | 
    ((stringr::str_sub(south_kanto_geometry$city_code, end=2) == '13') & (south_kanto_geometry$city_code <= "133086")),]
sf::st_write(south_kanto_geometry, '/home/rstudio/data_processing/geojson/south_kanto.geojson')
