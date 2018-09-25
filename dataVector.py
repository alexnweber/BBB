import numpy as np

def fixData(testX, testY, dataX, dataY, dataZ):
	N = len(testX)
	M = len(testY)
	L = len(dataX)
	testX = testX.repeat(M)
	testY = np.tile(testY, N)
	testX = testX.repeat(L)
	testY = testY.repeat(L)
	dataX = np.tile(dataX, N*M)
	dataY = np.tile(dataY, N*M)
	dataZ = np.tile(dataZ, N*M)
	return testX, testY, dataX, dataY, dataZ