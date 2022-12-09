from datetime import datetime, timedelta 
a,b,c=map(int,input('Enter your date of birth: ').split()
given_DOB=datetime(a,b,c)
current_date=datetime,today()
age_in_days=current_date-given_DOB
print('The no of days user lived',age_in_days.days)
