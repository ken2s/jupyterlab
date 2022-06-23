import imagej

# initialize imagej
ij = imagej.init(mode='interactive')
print(f"ImageJ2 version: {ij.getVersion()}")

# Load the image
url_colony = 'https://wsr.imagej.net/images/Cell_Colony.jpg'
cell_colony = ij.io().open(url_colony)

# Send the image to Python
xr_colony = ij.py.from_java(cell_colony)

# Display the image
ij.py.show(xr_colony, cmap='gray')

print(f"cell_colony type: {type(cell_colony)}")
print(f"xr_colony type: {type(xr_colony)}")

# load 4D test data
dataset = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_timeseries.tif')

# get xarray
xarr = ij.py.from_java(dataset)

# print out shape and dimensions
print(f"dataset dims, shape: {dataset.dims}, {dataset.shape}")
print(f"xarr dims, shape: {xarr.dims}, {xarr.shape}")

import skimage
import numpy as np

# load the image
astro_img = skimage.data.astronaut()

# Convert the image to a numpy array
astro_arr = ij.py.from_java(astro_img)

print(astro_arr.shape)

ij.py.show(astro_arr)
