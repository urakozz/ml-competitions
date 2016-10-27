import numpy as np
from sklearn.ensemble import RandomForestClassifier
import sys

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


#c = linear_model.SGDClassifier(loss="log", penalty="l2")
#c = linear_model.LogisticRegression(C=10)
#c = RandomForestClassifier(max_depth=20, n_estimators=100, max_features=1)
c = RandomForestClassifier(max_depth=20, n_estimators=100, max_features=1)
c.fit(X, y)
# scores = c.predict_proba(X)[:,1]
# print(metrics.roc_auc_score(y, scores))

n = int(input())
X_test = []
for _ in range(n):
    l = input().rstrip('\n').split(",")
    nums = [rev[h] for h in l]
    X_test.append(nums)



y_pred = c.predict(X_test)
for p in y_pred:
    print(int(p+1))