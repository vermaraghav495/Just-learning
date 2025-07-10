import numpy as np

data = np. random.rand(2,3,4)
zeroes = np.zeros ( (2,2,2))
full = np.full( (2,2,2), 7)
ones = np.ones ( (2,2,2) )

listl = np. random.rand(10)
list2 = np. random. rand ( 10)

add = np.add(listl, list2)
sub = np.subtract(listl, list2)
div = np.divide(listl, list2)
mult = np.multiply(listl, list2)
dot = np.dot(listl, list2)

sqrt = np.sqrt (25)
ab = np.abs (-2)
power = np. power (2,7)
log = np.log (25)
exp = np.exp([2,3])
mins = np.min(listl)
maxs= np.max(listl)

np.delete (data, 0, axis=1)
np.save("new array", data)
test = np.load("new array.npy")