from parameters import Standard

parser = Standard()

parser.setFEPolynomialDegree(4)
parser.setSpatialMax([1,2,3,4,5])
parser.snapshot()
parser.setTransportModel(True)

parser.saveAs("temp/inputSamples")