import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11) * 100
y = 2 * x + np.random.randn(10)*5
X = np.vstack((x,y))
print(X)
plt.scatter(X[0], X[1])
plt.show()
Xcentered = (X[0] - x.mean(), X[1] - y.mean())
m = (x.mean(), y.mean())
print(Xcentered)
print("Mean vector: ", m)
plt.scatter(Xcentered[0], Xcentered[1])
plt.show()
covmat = np.cov(Xcentered)
print(covmat, "\n")
print("Variance of X: ", np.cov(Xcentered)[0,0])
print("Variance of Y: ", np.cov(Xcentered)[1,1])
print("Covariance X and Y: ", np.cov(Xcentered)[0,1])
_, vecs = np.linalg.eig(covmat)
v = -vecs[:,1]
Xnew = np.dot(v, Xcentered)
print(Xnew)
v, v.shape
Xcentered
vecs[-1]
m
n = 9     #номер элемента случайной величины
Xrestored = np.dot(Xnew[n],v) + m
print('Restored: ', Xrestored)
print('Original: ', X[:,n])