from ast import While
from datetime import date
	
todays_date = date.today()

def get_dob():
    # write code here
	i = 0
	while(i < 3):
		try:
			if(i == 0):
				year = int(input("Enter year of birth: "))
			elif(i == 1):
				month = int(input("Enter month of birth: "))
			elif(i == 2):
				day = int(input("Enter day of birth: "))
		except:
			print("input is invalid. try again.")
		else:
			year_range = todays_date.year + 1
			if(i == 0):
				if year in range(0,year_range) :
					i+=1
				else:
					print("year is invalid. try again.")
			elif(i == 1):
				if month in range(1,13) :
					i+=1
				else:
					print("month is invalid. try again.")
			elif(i == 2):
				if day in range(1,31) :
					i+=1
				else:
					print("day is invalid. try again.")
	return {'year':year,'month':month,'day':day}


def get_age(dob):

    # write code here
	# ...
	age = todays_date.year - dob['year']
	if (todays_date.month < dob['month'] or (todays_date.month == dob['month'] and todays_date.day < dob['day'])):
		age -=1
	return age

def main():
	# write code here
	# ...
	while True:
		dob = get_dob()
		dob_compare = int(str(dob['year'])+str(dob['month']).rjust(2,"0")+str(dob['day']).rjust(2,"0"))
		today_compare = int(str(todays_date.year)+str(todays_date.month).rjust(2,"0")+str(todays_date.day).rjust(2,"0"))
		if(dob_compare<today_compare):
			print("You are {} years old.".format(get_age(dob)))
			break
		else:
			print("date of birth is invalid.")


if __name__ == '__main__':
    main()

