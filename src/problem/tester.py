from parameters import Standard

parser = Standard()

parser.setFEPolynomialDegree(4)
parser.setSpatialMax([1,2,3,4,5])
parser.setSpatialDimension(2)
parser.snapshot()
parser.setTransportModel(True)
parser.setOutputFilenameBase("howdy")
parser.saveAs("temp/inputSamples")