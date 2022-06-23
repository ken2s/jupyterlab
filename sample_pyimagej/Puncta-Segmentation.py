import imagej
import scyjava as sj

# initialize imagej
ij = imagej.init(mode='headless', add_legacy=True)
print(f"ImageJ version: {ij.getVersion()}")

# get additional resources
HyperSphereShape = sj.jimport('net.imglib2.algorithm.neighborhood.HyperSphereShape')
Overlay = sj.jimport('ij.gui.Overlay')
Table = sj.jimport('org.scijava.table.Table')
ParticleAnalyzer = sj.jimport('ij.plugin.filter.ParticleAnalyzer')

# load test data
# ds_src = ij.io().open('./test_still.tif')
ds_src = ij.io().open('https://raw.githubusercontent.com/imagej/pyimagej/master/doc/sample-data/test_still.tif')
ds_src = ij.op().convert().int32(ds_src) # convert image to 32-bit
ij.py.show(ds_src, cmap='binary')

# supress background noise
mean_radius = HyperSphereShape(5)
ds_mean = ij.dataset().create(ds_src.copy())
ij.op().filter().mean(ds_mean, ds_src.copy(), mean_radius)
ds_mul = ds_src * ds_mean
ij.py.show(ds_mul, cmap='binary')

# use gaussian subtraction to enhance puncta
img_blur = ij.op().filter().gauss(ds_mul.copy(), 1.2)
img_enhanced = ds_mul - img_blur
ij.py.show(img_enhanced, cmap='binary')

# apply threshold
img_thres = ij.op().threshold().renyiEntropy(img_enhanced)
ij.py.show(img_thres)

# convert ImgPlus to ImagePlus
imp_thres = ij.py.to_imageplus(img_thres)

# get ResultsTable and set ParticleAnalyzer
rt = ij.ResultsTable.getResultsTable()
ParticleAnalyzer.setResultsTable(rt)

# set measurements
ij.IJ.run("Set Measurements...", "area center shape")

# run the analyze particle plugin
ij.py.run_plugin(plugin="Analyze Particles...", args="clear", imp=imp_thres)

# convert results table -> scijava table -> pandas dataframe
sci_table = ij.convert().convert(rt, Table)
df = ij.py.from_java(sci_table)

# print dataframe
print(df)
