date = input("Enter the date in mm/dd/yyyy format : ")
date_list = date.split('/')
month_list = ['january','february','march','april','may','june','july','august','september','october','november','december']
print(month_list[int(date_list[0])]," ",date_list[1],",",date_list[2])

