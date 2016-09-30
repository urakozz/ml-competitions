# https://www.hackerrank.com/challenges/stockprediction
# http://stackoverflow.com/questions/1989992/predict-stock-market-values/1990555#1990555
import numpy as np 

m,k,d = [float(i) for i in input().split()]
k,d = int(k), int(d)
#print(m,k,d)
stock_names = []
stock_amount = []
stock_prices = []

for _ in range(k):
    line = input().split()
    stock_names.append(line[0])
    stock_amount.append(int(line[1]))
    stock_prices.append(np.array([float(i) for i in line[2:]]))
    
stock_prices = np.array(stock_prices)


slopes = np.zeros((k,2))
#slopes[:,0] = np.array([linregress(list(range(3)),line[1:4])[0] for line in stock_prices])
#slopes[:,1] = np.array([linregress(list(range(3)),line[2:])[0] for line in stock_prices])

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

def get_k(line):
    return np.array([(p - np.min(line))/(np.max(line)-np.min(line)) for p in line])
k_fast = np.array([get_k(line) for line in stock_prices])
ma_fast = np.array([moving_average(line) for line in k_fast])
#print(stock_prices)
#print(k_fast)
#print(ma_fast)
slopes[:,1] = np.subtract(k_fast[:,-1], k_fast[:,-2])
slopes[:,0] = np.subtract(k_fast[:,-2], k_fast[:,-3])
#print(slopes)



signals = np.subtract(slopes[:,1], slopes[:,0])
#print(signals)
last_prices = list(k_fast[:,-1])

signal_s, signal_b = np.array(last_prices), np.array(last_prices)

signal_s[signal_s < .5] = 0
signal_b[signal_b > .5] = 1
#print("s-b (1 - not)")
#print(len(signal_b), signal_b)
#print("s-s (0 - not)")
#print(len(signal_s), signal_s)

idx_b = np.argsort(signal_b)
idx_s = np.argsort(signal_s)[::-1]
#print("idx buy", idx_b)
#print("idx sell", idx_s)
buys = np.zeros((k,), dtype=int)
sells = np.zeros((k,), dtype=int)

for i in idx_b:
    if signal_b[i] == 1:
        # it's on the top history price, as well as next positions 
        break
    if k_fast[i][-1] > ma_fast[i][-1]:
        # price should be less then moving average
        continue
    if slopes[i][1] < slopes[i][0]:
        # velosity should grow
        continue
    price = stock_prices[i][-1]
    if price > m:
        continue
    amt = m // price
    buys[i] = amt
    break
    
for i in idx_s:
    if signal_s[i] == 0:
        # it's on the bottom history price
        break
    price = k_fast[i][-1]
    if price < ma_fast[i][-1]:
        # price should be greater then moving average
        continue
    if slopes[i][1] > slopes[i][0]:
        # velosity should go downwards
        continue
    if stock_amount[i] == 0:
        # no stocks :(
        continue
    sells[i] = stock_amount[i]

N = np.count_nonzero(np.c_[buys, sells])
print(N)
for i, b in enumerate(buys):
    if b > 0:
        print(stock_names[i], "BUY", b)
for i, s in enumerate(sells):
    if s > 0:
        print(stock_names[i], "SELL", s)
