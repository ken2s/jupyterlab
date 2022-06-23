import imagej

# initialize ImageJ in interactive mode
ij = imagej.init(mode='interactive')
print(f"ImageJ2 version: {ij.getVersion()}")

import skimage
import numpy as np

img = skimage.data.astronaut()
img = np.mean(img[10:190,140:310], axis=2)

ij.py.show(img, cmap = 'gray')

dataset_2d = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_still.tif')
ij.py.show(dataset_2d)

dataset_4d = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_timeseries.tif')
ij.py.show(dataset_4d[:, :, 2, 10]) # channel 2, frame 10

# get xarray from dataset
xarr_4d = ij.py.from_java(dataset_4d)
ij.py.show(xarr_4d[10, :, :, 2]) # channel 2, frame 10

import skimage
import numpy as np

img = skimage.data.astronaut()
img = np.mean(img[10:190,140:310], axis=2)
java_img = ij.py.to_java(img)

ij.ui().show(java_img)

dataset_2d = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_still.tif')
ij.ui().show(dataset_2d)

dataset_4d = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_timeseries.tif')
ij.ui().show(dataset_4d)

# get xarray from dataset
xarr_4d = ij.py.from_java(dataset_4d)
new_dataset_4d = ij.py.to_java(xarr_4d)
ij.ui().show(new_dataset_4d)
