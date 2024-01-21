#code
import math
t = int(input())
for _ in range(t):
    N = int(input())
    ans = 0
    while N:
        x = ((N&-N) << 1) - 1
        ans = x - ans
        N = N&(N-1)
    print(ans)
        
    
        