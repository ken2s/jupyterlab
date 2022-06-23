import imagej

# initialize imagej
ij = imagej.init()
print(f"ImageJ2 version: {ij.getVersion()}")

# first check if the legacy layer is active
print(f"Legacy layer active: {ij.legacy.isActive()}")

# demonstrate access to classes
print(ij.IJ)
print(ij.ResultsTable)
print(ij.RoiManager)
print(ij.WindowManager)
