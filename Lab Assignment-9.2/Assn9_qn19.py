class Time:
	def __init__(self,hh,mm,ss):
		self.hh = hh
		self.mm = mm
		self.ss = ss
	def __sub__(self,other):
		timediff = abs((self.hh*3600+self.mm*60+self.ss)-(other.hh*3600+other.mm*60+other.ss))
		hd = timediff//3600
		timediff = timediff-hd*3600
		md = timediff//60
		timediff = timediff-md*60
		return hd," HOUR ",md," MINUTE ",timediff," SECOND "
if __name__=="__main__":
	print("PLEASE ENTER THE TIME IN 24 HOUR FORMAT")
	print("INPUT-1")
	t1 = input("Enter 1st time in hh-mm-ss format\n")
	t1 = t1.split("-")
	ob1 = Time(int(t1[0]),int(t1[1]),int(t1[2]))
	print("INPUT-2")
	t2 = input("Enter 2nd time in hh-mm-ss format\n")
	t2 = t2.split("-")
	ob2 = Time(int(t2[0]),int(t2[1]),int(t2[2]))
	print("TIME DIFFERENCE = ",ob1-ob2)
