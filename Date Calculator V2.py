
import datetime
from dateutil.relativedelta import relativedelta

global today
today = datetime.date.today()

# Y/M/D Calculator
def Countdown(calcAge, name="", date=""):
	#Input or no
	if date == "":
		# User input version
		dateValid = False
		dateName = input("Date name: ")
		while not dateValid:
			userinput = input("Date (yyyy-mm-dd):")
			try:
				userdate = datetime.datetime.strptime(userinput, "%Y-%m-%d").date()
				dateValid = True
				break
			except:
				print("Try again!")
	else:
		dateName = name
		userdate = datetime.datetime.strptime(date, "%Y-%m-%d").date()

	# Check if date is in past or future
	pastORfuture = 0 # today|0, past|-1, future|1
	if today > userdate:
		pastORfuture = -1
	elif today == userdate:
		pastORfuture = 0
	else:
		pastORfuture = 1

	years = 0
	months = 0
	days = 0

	#change analysis positions
	def Position(date, numVal): 
		position = []
		if numVal == -1:
			position = [date, today]
		else:
			position = [today, date]
		return position

	pos = Position(userdate, pastORfuture)

	#Analyze date and output y/m/d
	if (userdate.month == 2) and (userdate.day == 29):
		if pastORfuture == -1: 
			days -= 1
		else:
			pass
	while (pos[0] < pos[1]):
		if pos[0] + relativedelta(years=1) > pos[1]:
			if pos[0] + relativedelta(months=1) > pos[1]:
				if pos[0] + relativedelta(days=1) > pos[1]:
					pass
				else:
					pos[0] += relativedelta(days=1)
					days += 1
			else:
				pos[0] += relativedelta(months=1)
				months += 1
		else:
			pos[0] += relativedelta(years=1)
			years += 1

	#Design y/m/d output
	def AgeTime(pastFuture, age):
		output = ["="]
		if pastFuture == -1:
			if age:
				output = ["is", "old"]
			else:
				output.append("ago")
		else:
			if age:
				output = ["has", "until born"]
			else:
				output.append("left")
		return output

	def YrMthDay(yrs, mths, days):
		output = ""
		if yrs == 1:
			output = "1 year, "
		elif yrs > 1:
			output = str(yrs)+" years, "
		else:
			pass

		if mths == 1:
			output += "1 month, "
		elif mths > 1:
			output += str(mths)+" months, "
		else:
			pass

		if days == 1:
			output += "1 day"
		elif days > 1:
			output += str(days)+" days"
		else:
			pass

		if mths == 0 or days == 0:
			output = output[:-2]

		return output

	#Print y/m/d output
	if pastORfuture == 0:
		print(dateName, "= TODAY")
	else:
		output1 = AgeTime(pastORfuture, calcAge)
		output2 = YrMthDay(years, months, days)

		print(dateName, output1[0], output2, output1[1])

def AgeTest(): #ask if date is for age or time (for user input)
	answer = input("Age or time?")
	if answer.lower().startswith("a"):
		answer = True
	else:
		answer = False
	Countdown(answer)

#Countdown(False, "Test", "2018-8-12")


# Percentage calculator (of today % in terms of progress between two dates)
def PercentCount(date1="", date2="", rounder=""):
	# Input or no
	if (date1 == ""): #User input mode
		dates = []
		for x in range(1, 3):
			dateValid = False
			while not dateValid:
				userinput = input("Date"+str(x)+" (yyyy-mm-dd):")
				try:
					userdate = datetime.datetime.strptime(userinput, "%Y-%m-%d").date()
					dateValid = True
					dates.append(userdate)
					break
				except:
					print("Try again!")
		date1 = dates[0]
		date2 = dates[1]
	else:
		date1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
		date2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()

	current_days = (today-date1).days
	total_days = (date2-date1).days
	
	if rounder == "":
		percentage = round(current_days/total_days * 100, 2)
	else:
		percentage = round(current_days/total_days * 100, int(rounder))

	return(str(percentage)+"%")
	