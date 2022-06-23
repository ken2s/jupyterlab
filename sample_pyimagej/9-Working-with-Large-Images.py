import imagej

ij = imagej.init(mode='interactive')
print(f"ImageJ2 version: {ij.getVersion()}")

from scyjava import jimport
Runtime = jimport('java.lang.Runtime')
def java_mem():
    rt = Runtime.getRuntime()
    mem_max = rt.maxMemory()
    mem_used = rt.totalMemory() - rt.freeMemory()
    return '{} of {} MB ({}%)'.format(int(mem_used)/2**20, int(mem_max/2**20), int(100*mem_used/mem_max))

java_mem()

big_data = ij.scifio().datasetIO().open('lotsofplanes&lengths=512,512,16,1000,10000&axes=X,Y,Channel,Z,Time.fake')

import numpy as np

dims = [big_data.dimension(d) for d in range(big_data.numDimensions())]
pix = np.prod(dims)
str(pix/2**40) + " terapixels"

java_mem()

def plane(image, pos):
    while image.numDimensions() > 2:
        image = ij.op().transform().hyperSliceView(image, image.numDimensions() - 1, pos[-1])
        pos.pop()
    return ij.py.from_java(ij.py.to_img(image))

ij.py.show(plane(big_data, [0, 0, 0]))

def axes(dataset):
    axes = {}
    for d in range(2, dataset.numDimensions()):
        axis = dataset.axis(d)
        label = axis.type().getLabel()
        length = dataset.dimension(d)
        axes[label] = length
    return axes

axes(big_data)

import matplotlib
import ipywidgets

widgets = {}
for label, length in axes(big_data).items():
    label = str(label) # HINT: Convert Java string to a python string to use with ipywidgets.
    widgets[label] = ipywidgets.IntSlider(description=label, max=length-1)

widgets

def f(**kwargs):
    matplotlib.pyplot.imshow(plane(big_data, list(kwargs.values())), cmap='gray')
ipywidgets.interact(f, **widgets)
