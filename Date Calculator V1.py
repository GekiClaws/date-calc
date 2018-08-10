  
import datetime
from dateutil.relativedelta import relativedelta

def DetermineDate(years_until_next_leap_year, date, days, future_or_past): 
        today = datetime.date.today()
        z = future_or_past
        y = 0
        m = 0
        x = 4 - years_until_next_leap_year 
        while (days > 365):
                if x%4 == 0:
                        days = days - 366
                else:
                        days = days - 365
                y = y+1
                x = x+1       
        date1 = date + relativedelta(years=y)
        if z == 1:
                while (date1 < today):
                        date1 = date1+relativedelta(months=1)
                        m = m+1
                if date1 > today:
                        date1 = date1-relativedelta(months=1)
                        m = m-1
                else:
                        pass
                days = (today - date1).days
        else:
                while (date1 > today):
                        today = today+relativedelta(months=1)
                        m = m+1
                if date1 < today:
                        today = today-relativedelta(months=1)
                        m = m-1
                else:
                        pass
                days = (date1-today).days
                
        # return multiple values
        result = [y]
        result.append(m)
        result.append(days)
        return result

def PastFuture(DateName, date, years_until_next_leap_year):
        x = 0
        today = datetime.date.today()

        if date > today:
                days = (date - today).days #days left
                x = 0
        else:
                days = (today - date).days #days ago
                x = 1

        result = DetermineDate(years_until_next_leap_year, date, days, x)
        y = result[0]
        m = result[1]
        d = result[2]
        if x == 0: #days left
                if y == 1:
                        if m == 1:
                                if d == 1:
                                        print(DateName, "=", y, "year,", m, "month, and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", y, "year,", m, "month, and", d, "days left")
                                else:
                                        print(DateName, "=", y, "year and", m, "month left")
                        elif m > 0:
                                if d == 1:
                                        print(DateName, "=", y, "year,", m, "months, and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", y, "year,", m, "months, and", d, "days left")
                                else:
                                        print(DateName, "=", y, "year and", m, "months left")
                                
                        else:
                                if d == 1:
                                        print(DateName, "=", y, "year and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", y, "year and", d, "days left")
                                else:
                                        print(DateName, "=", y, "year left")
                elif y > 0:
                        if m == 1:
                                if d == 1:
                                        print(DateName, "=", y, "years,", m, "month, and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", y, "years,", m, "month, and", d, "days left")
                                else:
                                        print(DateName, "=", y, "years and", m, "month left")
                        elif m > 0:
                                if d == 1:
                                        print(DateName, "=", y, "years,", m, "months, and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", y, "years,", m, "months, and", d, "days left")
                                else:
                                        print(DateName, "=", y, "years and", m, "months left")
                                
                        else:
                                if d == 1:
                                        print(DateName, "=", y, "years and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", y, "years and", d, "days left")
                                else:
                                        print(DateName, "=", y, "years left")
                
                else:
                        if m == 1:
                                if d == 1:
                                        print(DateName, "=", m, "month, and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", m, "month, and", d, "days left")
                                else:
                                        print(DateName, "=", m, "month left")
                        elif m > 0:
                                if d == 1:
                                        print(DateName, "=", m, "months, and", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", m, "months, and", d, "days left")
                                else:
                                        print(DateName, "=", m, "months left")
                                
                        else:
                                if d == 1:
                                        print(DateName, "=", d, "day left")
                                elif d > 0:
                                        print(DateName, "=", d, "days left")
                                else:
                                        print(DateName, "= TODAY!")
        else: #days ago
                if y == 1:
                        if m == 1:
                                if d == 1:
                                        print(DateName, "=", y, "year,", m, "month, and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", y, "year,", m, "month, and", d, "days ago")
                                else:
                                        print(DateName, "=", y, "year and", m, "month ago")
                        elif m > 0:
                                if d == 1:
                                        print(DateName, "=", y, "year,", m, "months, and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", y, "year,", m, "months, and", d, "days ago")
                                else:
                                        print(DateName, "=", y, "year and", m, "months ago")
                                
                        else:
                                if d == 1:
                                        print(DateName, "=", y, "year and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", y, "year and", d, "days ago")
                                else:
                                        print(DateName, "=", y, "year ago")
                elif y > 0:
                        if m == 1:
                                if d == 1:
                                        print(DateName, "=", y, "years,", m, "month, and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", y, "years,", m, "month, and", d, "days ago")
                                else:
                                        print(DateName, "=", y, "years and", m, "month ago")
                        elif m > 0:
                                if d == 1:
                                        print(DateName, "=", y, "years,", m, "months, and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", y, "years,", m, "months, and", d, "days ago")
                                else:
                                        print(DateName, "=", y, "years and", m, "months ago")
                                
                        else:
                                if d == 1:
                                        print(DateName, "=", y, "years and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", y, "years and", d, "days ago")
                                else:
                                        print(DateName, "=", y, "years ago")
                
                else:
                        if m == 1:
                                if d == 1:
                                        print(DateName, "=", m, "month, and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", m, "month, and", d, "days ago")
                                else:
                                        print(DateName, "=", m, "month ago")
                        elif m > 0:
                                if d == 1:
                                        print(DateName, "=", m, "months, and", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", m, "months, and", d, "days ago")
                                else:
                                        print(DateName, "=", m, "months ago")
                                
                        else:
                                if d == 1:
                                        print(DateName, "=", d, "day ago")
                                elif d > 0:
                                        print(DateName, "=", d, "days ago")
                                else:
                                        print(DateName, "= TODAY!")

def CalculateAge(Name, date, years_until_next_leap_year):
        today = datetime.date.today()
        
        days = (today - date).days #past
        x = 1

        result = DetermineDate(years_until_next_leap_year, date, days, x)
        y = result[0]
        m = result[1]
        d = result[2]
        if y == 1:
                if m == 1:
                        if d == 1:
                                print(Name, "is", y, "year,", m, "month, and", d, "day old")
                        elif d > 0:
                                print(Name, "is", y, "year,", m, "month, and", d, "days old")
                        else:
                                print(Name, "is", y, "year and", m, "month old")
                elif m > 0:
                        if d == 1:
                                print(Name, "is", y, "year,", m, "months, and", d, "day old")
                        elif d > 0:
                                print(Name, "is", y, "year,", m, "months, and", d, "days old")
                        else:
                                print(Name, "is", y, "year and", m, "months old")
                                
                else:
                        if d == 1:
                                print(Name, "is", y, "year and", d, "day old")
                        elif d > 0:
                                print(Name, "is", y, "year and", d, "days old")
                        else:
                                print(Name, "is", y, "year old")
        elif y > 0:
                if m == 1:
                        if d == 1:
                                print(Name, "is", y, "years,", m, "month, and", d, "day old")
                        elif d > 0:
                                print(Name, "is", y, "years,", m, "month, and", d, "days old")
                        else:
                                print(Name, "is", y, "years and", m, "month old")
                elif m > 0:
                        if d == 1:
                                print(Name, "is", y, "years,", m, "months, and", d, "day old")
                        elif d > 0:
                                print(Name, "is", y, "years,", m, "months, and", d, "days old")
                        else:
                                print(Name, "is", y, "years and", m, "months old")
                                
                else:
                        if d == 1:
                                print(Name, "is", y, "years and", d, "day old")
                        elif d > 0:
                                print(Name, "is", y, "years and", d, "days old")
                        else:
                                print(Name, "is", y, "years old")
                
        else:
                if m == 1:
                        if d == 1:
                                print(Name, "is", m, "month, and", d, "day old")
                        elif d > 0:
                                print(Name, "is", m, "month, and", d, "days old")
                        else:
                                print(Name, "is", m, "month old")
                elif m > 0:
                        if d == 1:
                                print(Name, "is", m, "months, and", d, "day old")
                        elif d > 0:
                                print(Name, "is", m, "months, and", d, "days old")
                        else:
                                print(Name, "is", m, "months old")
                                
                else:
                        if d == 1:
                                print(Name, "is", d, "day old")
                        elif d > 0:
                                print(Name, "is", d, "days old")
                        else:
                                print(Name, "was born today.")
        
# Test Date #
date = datetime.date(2010, 1, 1)
PastFuture("TestDate", date, 2)
