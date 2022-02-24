def pin(s):
    c = 0
    co = 0
    for i in s:
        if i==' ':
            continue
        else:
            c=c+1
    while c>9:
        while c>0:
            r = c%10
            co = co+r
            c=c//10
        c=co
    return c
name = input("Enter your name : ")
print("PIN = ",pin(name))