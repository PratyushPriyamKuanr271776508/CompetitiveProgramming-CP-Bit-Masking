#code
def xorSort(A, B, C):
    maxBitLen = max((A).bit_length(), (B).bit_length(), (C).bit_length())
    ans = 0
    mask = 1 << maxBitLen
    
    i = mask
    
    if A <= B <= C: return 0
    if A == C and A != B: return -1
    
    # Iterating till we find different bits
    a = 0
    b = 0
    c = 0
    while i and a == b == c:
        a = A&i
        b = B&i
        c = C&i
        i >>= 1
    
    a_set = 0
    
    if i == 0: i = 1
    else: i <<= 1
    
    if (a,b,c) in {(i,0,i),(0,i,0)}: return -1
    elif (a,b,c) in {(0,i,i),(i,0,0)}: 
        a_set = 1
        if a == i: ans |= i
        i >>= 1
        if B == C: return ans
    else:
        if c == 0: ans |= i
        i >>= 1
        if A == B: return ans

    if a_set == 1:
        b = tb = B&i
        c = tc = C&i

        while i and b == c: 
            b = B&i
            c = C&i
            i >>= 1
        if i == 0: i = 1
        elif tb != b or tc != c: i <<= 1
        if b != 0: ans |= i
    else:
        a = ta = A&i
        b = tb = B&i
        while i and a == b:
            a = A&i
            b = B&i
            i >>= 1
        if i == 0: i = 1
        elif tb != b or ta != a: i <<= 1
        if a != 0: ans |= i
    
    return ans
    
t = int(input())
for _ in range(t):
    A, B, C = (int(x) for x in input().split())
    print(xorSort(A, B, C))
    