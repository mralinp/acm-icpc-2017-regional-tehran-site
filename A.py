while(True):
    a, b = list(map(int, input().split(" ")))
    if(a == 0 and b == 0):
        break
    res = min(a*30 + b*40, a*35 + b*40)
    res = min(res, a*40 + b*20)
    print (res)