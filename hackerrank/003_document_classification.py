# https://www.hackerrank.com/challenges/document-classification

__author__ = 'yury.kozyrev'

import numpy as np
from sklearn import feature_extraction
from sklearn import svm
# from sklearn.metrics import accuracy_score

X,y = [],[]
with open("trainingdata.txt", "r") as f:
    n = int(f.readline())
    for _ in range(n):
        l = f.readline()
        y.append(int(l[0]))
        X.append(l[2:].strip())

X, y = np.array(X), np.array(y)

vector_text = feature_extraction.text.TfidfVectorizer(min_df=5)
X = vector_text.fit_transform(X)

c = svm.SVC(kernel='linear')
c.fit(X, y)

n = int(input())
X_test = []
for _ in range(n):
    X_test.append(input())
X_test = vector_text.transform(X_test)

y_pred = c.predict(X_test)
for p in y_pred
