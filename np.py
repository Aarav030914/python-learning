import numpy
import sys
a = numpy.array([[1,2,4,4,5,6], [7,8,9,10,11,12]])
numpy.save('sample_np', a)
b = numpy.load("sample_np.npy")
print(b)