library(ggplot2)
library(sf)

# Read the night lights shapefile
night_lights_df <- read_sf('./data_processing/output/')

# Visualize the mean light values
ggplot(data = night_lights_df) +
  geom_sf(aes(fill=mean_light), lwd=0) +
  scale_fill_viridis_c() +
  theme_void()
