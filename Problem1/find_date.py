import datetime
from datetime import date 
def findDay(date):
    day, month, year = (int(i) for i in date.split('/'))   
    born = datetime.date(year, month, day)
    return born.strftime("%A")

date = input()
print(findDay(date))