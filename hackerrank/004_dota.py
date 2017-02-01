import numpy as np
from sklearn import neural_network
from sklearn import metrics
import sys

from sklearn.ensemble import RandomForestClassifier

X,y = [],[]
heroes = []
rev = dict()
with open("trainingdata.txt", "r") as f:
    for line in f:
        l = line.rstrip('\n').split(",")
        ans = int(l[-1]) - 1

        for hero in l[:-1]:
            if hero not in rev:
                rev[hero] = len(heroes)
                heroes.append(hero)
        nums = [rev[h] for h in l[:-1]]
        X.append(nums)
        y.append(ans)

X, y = np.array(X), np.array(y)
X_oh = np.zeros((X.shape[0], len(heroes)*2))
for i, row in enumerate(X):
    for h in row[:5]:
        X_oh[i,h] = 1
    for h in row[5:]:
        X_oh[i,len(heroes)+h] = 1

#c = linear_model.SGDClassifier(loss="log", penalty="l2")
#c = linear_model.LogisticRegression(C=10)
c = RandomForestClassifier(max_depth=20, n_estimators=100, max_features=1)
c = neural_network.MLPClassifier((256,16))
c.fit(X_oh, y)
# scores = c.predict_proba(X_oh)[:,1]
# print(metrics.roc_auc_score(y, scores))

n = int(input())
X_test = []
for _ in range(n):
    l = input().rstrip('\n').split(",")
    nums = [rev[h] for h in l]
    X_test.append(nums)

X_test_oh = np.zeros((len(X_test), len(heroes)*2))
for i, row in enumerate(X_test):
    for h in row[:5]:
        X_test_oh[i,h] = 1
    for h in row[5:]:
        X_test_oh[i,len(heroes)+h] = 1

y_pred = c.predict(X_test_oh)
for p in y_pred:
    print(int(p+1))