import imagej

# initialize ImageJ2
ij = imagej.init(mode='interactive')
print(f"ImageJ2 version: {ij.getVersion()}")

# load local test data
dataset = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_timeseries.tif')

# load web test data
web_image = ij.io().open('https://wsr.imagej.net/images/Cell_Colony.jpg')

# show the web image
ij.py.show(web_image)

# show the 4D dataset in ImageJ's viewer
ij.ui().show(dataset)

def dump_info(image):
    """A handy function to print details of an image object."""
    name = image.name if hasattr(image, 'name') else None # xarray
    if name is None and hasattr(image, 'getName'): name = image.getName() # Dataset
    if name is None and hasattr(image, 'getTitle'): name = image.getTitle() # ImagePlus
    print(f" name: {name or 'N/A'}")
    print(f" type: {type(image)}")
    print(f"dtype: {image.dtype if hasattr(image, 'dtype') else 'N/A'}")
    print(f"shape: {image.shape}")
    print(f" dims: {image.dims if hasattr(image, 'dims') else 'N/A'}")

dump_info(dataset)

# convert the ImageJ image (Java) to an xarray.DataArray (Python)
xarr = ij.py.from_java(dataset)

# dump info on xarray.DataArray result from ij.py.from_java()
dump_info(xarr)

import skimage
cells = skimage.data.cells3d()
dump_info(cells)

import xarray
xcells = xarray.DataArray(cells, name='xcells', dims=('pln', 'ch', 'row', 'col'))
dump_info(xcells)

# send image data to Java
jcells = ij.py.to_java(cells)
jxcells = ij.py.to_java(xcells)

# dump info
print("[jcells]")
dump_info(jcells)
print("\n[jxcells]")
dump_info(jxcells)

# convert jxcells back to Python
xcells_2 = ij.py.from_java(jxcells)

print("[xcells - original Python image]")
dump_info(xcells)
print("\n[jxcells - after conversion to Java]")
dump_info(jxcells)
print("\n[xcells_2 - conversion back to Python]")
dump_info(xcells_2)

# slice the test data
java_slice = dataset[:, :, 1, 10]
python_slice = xarr[10, :, :, 1]

# print slice shape
print(f"java_slice: {java_slice.shape}")
print(f"python_slice: {python_slice.shape}")

print(f"java_slice type: {type(java_slice)}")

# wrap as ImgPlus -- you can also wrap the slice as a dataset with ij.py.to_dataset()
img = ij.py.to_img(java_slice)
ij.py.show(img)

print(f"python_slice type: {type(python_slice)}")

# xarray images can just be displayed
ij.py.show(python_slice)

# get two slices from the test dataset
xarr_slice1 = xarr[12, :, :, 1]
xarr_slice2 = xarr[12, :, :, 2]

# these slices should only be 2D (i.e. x,y)
print(f"s1 shape: {xarr_slice1.shape}")
print(f"s2 shape: {xarr_slice2.shape}")

import xarray as xr

# note that you must specify which coordnate ('dim') to concatenate on
new_stack = xr.concat([xarr_slice1[:,:], xarr_slice2[:,:]], dim='ch')

print(f"Number of dims: {len(new_stack.dims)}\ndims: {new_stack.dims}\n shape: {new_stack.shape}")

# view the data
ij.py.show(new_stack[0])
ij.py.show(new_stack[1])

# send new_stack back to ImageJ/Java
img = ij.py.to_java(new_stack)
print(f"img dims: {img.dims}\nimg shape: {img.shape}")

import scyjava as sj

Views = sj.jimport('net.imglib2.view.Views')

jslice_1 = dataset[:, :, 1, 12]
jslice_2 = dataset[:, :, 2, 12]
print(f"slice 1 shape: {jslice_1.shape}\nslice 2 shape: {jslice_2.shape}")

jstack = Views.stack(jslice_1, jslice_2)
print(f"stack shape: {jstack.shape}")

# view the two slices jstack
ij.py.show(ij.py.to_img(jstack[:, :, 0]))
ij.py.show(ij.py.to_img(jstack[:, :, 1]))

# initialize a new numpy array with numpy array
new_arr1 = ij.py.initialize_numpy_image(xarr.data)

# initialize a new numpy array with xarray
new_arr2 = ij.py.initialize_numpy_image(xarr)

# initialize a numpy array with RandomeAccessibleInterval
new_arr3 = ij.py.initialize_numpy_image(dataset)

print(f"xarr/numpy shape: {xarr.shape}\ndataset shape: {dataset.shape}")
print(f"new_arr1 shape: {new_arr1.shape}\nnew_arr2 shape: {new_arr2.shape}\nnew_arr3 shape: {new_arr3.shape}")

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr_output = ij.py.initialize_numpy_image(arr1)

ij.op().run('multiply', ij.py.to_java(arr_output), ij.py.to_java(arr1), ij.py.to_java(arr2))
print(arr_output) # this output will be [[5, 12], [21, 32]]

print(ij.window().getOpenWindows())

ij.window().clear()
