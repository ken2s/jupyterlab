import imagej

# initialize ImageJ
ij = imagej.init('sc.fiji:fiji:2.5.0')
print(f"ImageJ version: {ij.getVersion()}")

import numpy as np

array = np.random.rand(5, 4, 3)
dataset = ij.py.to_java(array)

print(dataset.shape)

ij.getApp().getInfo(True)
