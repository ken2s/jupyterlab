import imagej
import scyjava as sj

# initialize ImageJ2
ij = imagej.init(mode='interactive')
print(f"ImageJ2 version: {ij.getVersion()}")

# import ImageJ classes
IJ = sj.jimport('ij.IJ')
ImagePlus = sj.jimport('ij.ImagePlus')

# open test image and convert from Dataset to ImagePlus
dataset = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_still.tif')
imp = ij.convert().convert(dataset, ImagePlus)

# show the image
ij.py.show(imp)

# show image and then find maxima
imp.getProcessor().resetMinAndMax()
ij.ui().show(imp)
IJ.run(imp, "Find Maxima...", "prominence=1000 output=[Point Selection]")

# get ImageJ's duplicator
Duplicator = sj.jimport('ij.plugin.Duplicator')

# run ImageJ commands
imp_timeseries = IJ.openImage("https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_timeseries.tif")
imp_extract = Duplicator().run(imp_timeseries, 3, 3, 1, 1, 14, 14) # visit the Javadoc for more info https://imagej.nih.gov/ij/developer/api/ij/ij/plugin/Duplicator.html
IJ.run(imp_extract, "Enhance Contrast", "saturated=0.35")
ij.ui().show(imp_extract)
IJ.setAutoThreshold(imp_extract, "Moments dark")
IJ.run(imp_extract, "Analyze Particles...", " show=Overlay display clear")
