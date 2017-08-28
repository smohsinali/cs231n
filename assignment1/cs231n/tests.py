import numpy as np
from past.builtins import xrange

x = np.array([[5, 6], [3, 5]])
y = np.array([[5, 2], [1, 2], [4 ,2]])

# num_test = x.shape[0]
# num_train = y.shape[0]
# dists = np.zeros((num_test, num_train))
# print("hi")
# # print(X[0:10 , :])
# for i in xrange(num_test):
#   for j in xrange(num_train):
#     dists[i, j] = np.sqrt(np.sum(np.square(x[i, :] - y[j, :])))
#
# print("dists", dists)
#
# new_dists = np.zeros((num_test, num_train))
# m1 = -2 * np.dot(x, y.T)
# print("m1", m1)
# m2 = np.diag(np.dot(x, x.T))
# m2 = m2.reshape((-1, 1))
# print("m2", m2)
# m3 = np.diag(np.dot(y, y.T))
# # m3 = m3.reshape((-1, 1))
# print("m3", m3)
#
# dists2 = np.sqrt(m1+m2+m3)
# print("dists", dists2)

num_folds=5
x = np.arange(20)
x_new = np.array_split(x, num_folds)
y = range(num_folds)
for i in range(num_folds):
  new_data = []
  new_test = []
  for j in range(num_folds):
    if j==i:
      new_test.extend(x_new[j])
    else:
      new_data.extend(x_new[j])

  print("loop", i, ":", new_data, new_test)

  # print(np.array_split(x, 1))
