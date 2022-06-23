import imagej

# initialize ImageJ in interactive mode
ij = imagej.init(mode='interactive')
print(f"ImageJ2 version: {ij.getVersion()}")

# create lists
python_list = [1, 2, 3, 4]
java_list = ij.py.to_java(python_list)

# modify one list
python_list[0] = 4

# check list contents
print(f"python_list: {python_list}\njava_list: {java_list}")

print("List values:")
for i in range(len(python_list)):
    print(f"python: {python_list[i]}, java: {java_list[i]}")

from jpype import JArray, JInt

java_int_array = JArray(JInt)([1, 2, 3, 4])

print(f"type: {type(java_int_array)}\nvalue: {java_int_array}")

import numpy as np

# get numpy array and list
test_arr = np.array([[5, 12], [21, 32]])
test_list = [1, 2, 4, 8, 16, 32, 64]

# convert array and list to Java
jarr = ij.py.to_java(test_arr)
jlist = ij.py.to_java(python_list)

print(type(jarr))
print(type(jlist))

import scyjava as sj

# import RandomAccessibleInterval class
RandomAccessibleInterval = sj.jimport('net.imglib2.RandomAccessibleInterval')

print(f"jarr: {isinstance(jarr, RandomAccessibleInterval)}")
print(f"jlist: {isinstance(jlist, RandomAccessibleInterval)}")

# Import an image with scikit-image.
# NB: Blood vessel image from: https://www.fi.edu/heart/blood-vessels
from skimage import io

url = 'https://www.fi.edu/sites/fi.live.franklinds.webair.com/files/styles/featured_large/public/General_EduRes_Heart_BloodVessels_0.jpg'
img = io.imread(url)
img = np.mean(img, axis=2)

# show image
ij.py.show(img)

result = np.zeros(img.shape)
# these sigmas will be nice for the larger sections
sigma1 = 8
sigma2 = 2
# note the use of to_java on img and result to turn the numpy images into RAIs
ij.op().filter().dog(ij.py.to_java(result), ij.py.to_java(img), sigma1, sigma2)
# purple highlights the edges of the vessels, green highlights the centers
ij.py.show(result, cmap = 'PRGn')