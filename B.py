while(True):
    l = list(input().split(" "))
    ans =  0
    if(l == ["0000", "0000", "0000", "0000"]):
        break
    for i in l:
        for j in range(4):
            if((j+1)%2 == 0):
                ans += int(i[j])
            else:
                t = int(i[j])
                t*=2
                if(t > 9):
                    t-=9
                ans += t
    if(ans % 10 == 0):
        print ("Yes")
    else:
        print ("No")