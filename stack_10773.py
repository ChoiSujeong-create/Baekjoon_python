from sys import stdin
s = 0
n = int(stdin.readline())
financial_ledger = list()
for i in range(n):
    num = int(stdin.readline())
    if num == 0:
        del financial_ledger[-1]
    else:
        financial_ledger.append(num)

for idx in range(len(financial_ledger)):
    s += financial_ledger[idx]
print(s)
