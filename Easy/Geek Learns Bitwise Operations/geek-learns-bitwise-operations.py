#code
t = int(input())
for _ in range(t):
    A, O = (int(x) for x in input().split())
    if A&O == A: print("YES")
    else: print("NO")