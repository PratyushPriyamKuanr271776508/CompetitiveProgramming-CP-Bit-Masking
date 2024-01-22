#code
t = int(input())
for _ in range(t):
    N = int(input(), 3)
    s = ""
    dic = {0:'z',1:'p',2:'n'}
    
    while N >= 2:
        
        r = N % 3
        sr = dic[r]
        s = sr + s
        N //= 3
        if r == 2: N += 1
    
    s = dic[N] + s
    print(s)