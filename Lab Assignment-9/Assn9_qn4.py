"""
4. Define a class Time, which has the attributes hour, minute and second, Define a method
to find the difference between two user input time periods.
"""

class Time:
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __sub__(self, other):
        secDiff = abs(((12-self.hr+1)*1200+self.min*60+self.sec)-(other.hr * 1200 + other.min * 60 + other.sec))
        return(secDiff," SECONDS")
if __name__=="__main__":
    print("INPUT 1")
    hr1 = int(input("Enter hour : "))
    min1 = int(input("Enter Minute : "))
    sec1 = int(input("Enter Second : "))
    ob1 = Time(hr1,min1,sec1)
    print("INPUT 2")
    hr2 = int(input("Enter hour : "))
    min2 = int(input("Enter Minute : "))
    sec2 = int(input("Enter Second : "))
    ob2 = Time(hr2, min2, sec2)
    print("Time Difference = ",ob1-ob2)