
# Read the night lights shapefile
night_lights_df <- sf::read_sf('./data_processing/output/')

# Visualize the mean light values
plot(night_lights_df)
