#code
from functools import reduce
t = int(input())
for _ in range(t):
    N = int(input())
    ls = [int(x) for x in input().split()]
    print(reduce(lambda x, y: x^y, ls))