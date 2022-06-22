def get_sum(a,b):
    if a == b:
        return a
    elif a > b >= 0:
        r = 0
        for n in range(b, a+1, 1):
            r += n
        return r
    elif a < b:
        r = 0
        for n in range(b, a-1, -1):
            r += n
        return r
    elif  b < 0:
        r = 0
        for n in range(a, b-1, -1):
            r += n
        return r