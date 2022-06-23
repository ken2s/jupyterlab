import imagej

# initialize ImageJ
ij = imagej.init()
print(f"ImageJ2 version: {ij.getVersion()}")

print(ij.op().help('filter.addPoissonNoise'))

from skimage import io

# Create a numpy image using scikit
img = io.imread('https://imagej.net/images/clown.jpg')

ij.py.show(img)
print(type(ij.py.to_java(img)))

import numpy as np

result = np.zeros(img.shape) # HINT: Uses float dtype, for more accurate noising.

imgIterable = ij.op().transform().flatIterableView(ij.py.to_java(img))
resIterable = ij.op().transform().flatIterableView(ij.py.to_java(result))

ij.op().filter().addPoissonNoise(resIterable, imgIterable)

ij.py.show(result)

# grab the RGB values in a line from [0][5] to [0][10] in our image
print(result[0][5:10])

ij.py.show(img.astype(int))
       
result = np.clip(result, 0, 255)
ij.py.show(result.astype(np.uint8))

# print is required to render new lines
print(ij.op().help('multiply'))
