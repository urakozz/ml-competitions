# https://www.hackerrank.com/challenges/predicting-office-space-price
# python3

import numpy as np
from sklearn.preprocessing import PolynomialFeatures

F,N = [int(i) for i in input().split()]
l = []
l_ = []

for _ in range(N):
	l.append([float(i) for i in input().split()])

T = int(input())
for _ in range(T):
	l_.append([float(i) for i in input().split()])

X = np.array(l)
X_ = np.array(l_)
one = [[1]]*N
one_ = [[1]]*T

y = X[:,F:F+1]
X = X[:,:F]

poly = PolynomialFeatures(3)
X = poly.fit_transform(X)
X_ = poly.fit_transform(X_)

B = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(y))

for p in np.dot(X_, B).reshape(-1):
    print (round(p, 2))
