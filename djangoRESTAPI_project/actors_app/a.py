import pandas as pd
import calendar
from datetime import datetime
datem = datetime.today().strftime("%Y-%m")
yearmonth = datem.split('-')
month_count  = calendar.monthrange(int(yearmonth[0]),int(yearmonth[1]))[1]
count =0
for day in range(1, month_count+1):
        presentday = datetime(int(yearmonth[0]), int(yearmonth[1]), day)
        if presentday.strftime('%A') not in ["Saturday","Sunday"]:
            count = count+1

completed_in_a_month = count*9
print("Hours completed in a month "+str(completed_in_a_month))


completed_as_of_now = sum(df['Completed Work'])
print("completed hours as of now "+ str(completed_as_of_now ))

print("Number of hours pending "+ str(completed_in_a_month - completed_as_of_now))