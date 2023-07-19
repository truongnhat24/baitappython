# Date and Time Exercise - Exercise 4: Print a date in a the following format
from datetime import datetime
given_date = datetime(2020, 2, 25)
print(given_date.strftime('%A %d %B %Y'))