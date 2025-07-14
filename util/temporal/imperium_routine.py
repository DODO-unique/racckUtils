import time


def isLeap(year):
    if year%400==0 or (year%100!=0 and year%4==0):
        return True
    else:
        return False

current_time=int(time.time())
years= int(current_time/31556926)
print(1970+years)
this_year=1970+years
#This is inaccurate because the number of seconds in a year is taken as 365.2422
# seconds_this_year=(current_time-((years)*31556926))

_inSeconds=0
# We need precise numbers for this here, so we run a loop
for i in range (1970, 1970+years):
    if isLeap(i):
        _inSeconds+=31622400
    else:
        _inSeconds+=31536000

print(f"{current_time} this is the curren ttime")
print(f"{_inSeconds} this is _inseconds")
seconds_this_year=0
seconds_this_year=current_time-_inSeconds

print(seconds_this_year)

#I have a gut feelign there is a better way to handle this than the loop...
mCount=0
month=0
while True:
    mCount+=1
    if mCount in (1,3,5,7,8,10,12):
        seconds_this_year-=2678400
    elif mCount in (4,6,9,11):
        seconds_this_year-=2592000
    elif mCount==2:
        if isLeap(this_year):
            seconds_this_year-=2505600
        else:
            seconds_this_year-=2419200
    if seconds_this_year<2419200:
        month=mCount+1
        break

days_this_month = 0
days_this_month = int(seconds_this_year/86400)
if seconds_this_year%86400 != 0:
    days_this_month+=1


hours_today = int((seconds_this_year%86400)/3600)
if (seconds_this_year%86400)/3600 > hours_today:
    minutes=int(((seconds_this_year%86400)-(hours_today*3600))/60)
    seconds=((seconds_this_year%86400)-(hours_today*3600))-(minutes*60)

print(f"{this_year} is the current year")
print(f"{seconds_this_year} is the current year in seconds")
print(f"{month} is the current month number")
print(f"{days_this_month} is the number of days past")
print(f"{hours_today} is the number of hours past today")
print(f"{minutes} is the number of minutes past today")
print(f"{seconds} is the number of seconds past today")




    

# month= (current_time-(years*31556926))/2629743 
# #okay, this is complicated because it can get hella confusing because that is the average days in a month and not the exact number
#that's why we first go days, then therough it we go months
#days in the current year, so we cur the previous years down and start with this year's time.
