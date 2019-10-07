# -*- encoding: utf-8

from datetime import datetime, timedelta

birthday = [datetime(2001,1,1),
            datetime(2002,2,2),
            datetime(2003,3,3)]
today = datetime.today().year
one_year = 365.25
for element in birthday:
    age = (today - element.year)
    print (age)

for i in range(len(birthday)):
    age = (today - birthday[i].year)
    print (age)

i = 0
while i < len(birthday):
    age = (today - birthday[i].year)
    print (age)
    i+=1