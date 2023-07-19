# Date and Time Exercise - Exercise 2: Convert string into a datetime object
import datetime
date_string = "Feb 25 2020 4:20PM"
print(datetime.datetime.strptime(date_string, '%b %d %Y %I:%M%p'))