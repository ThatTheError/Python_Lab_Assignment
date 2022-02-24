class cntObj:
    cnt = 0
    def __init__(self):
        cntObj.cnt+=1
if __name__=="__main__":
    while True:
        ch = int(input("1. Create object \n0. Exit\n"))
        if ch==1:
            cntObj()
        elif ch==0:
            break
        else:
            print("Invalid Choice")
    print("Number of object crated = ",cntObj.cnt)
