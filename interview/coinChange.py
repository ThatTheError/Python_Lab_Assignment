def coinChange(amt):
    list1 = [5,4,2,1]
    changelist = list()
    for i in range(0,len(list1)):   #20
        c = 0
        while amt>=list1[i]:
            amt -= list1[i]
            c+=1
        changelist.append(c)
    for i in range(0,len(list1)):
        if changelist[i] > 0:
            print(list1[i],"=",changelist[i])
if __name__=="__main__":
    amt = int(input("Enter the main Amount"))
    coinChange(amt)