#Date Finder
import datetime

#Default : get the data for next Monday
#(Can be expanded for explicit clinic days)
def next_monday():
    today = datetime.date.today()
    days_until_monday = (7 - today.weekday()) % 7
    next_monday_date = today + datetime.timedelta(days=days_until_monday)
    return next_monday_date.strftime("%d%m%y")
