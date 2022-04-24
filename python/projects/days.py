months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 30,
    "September": 31,
    "October": 31,
    "November": 30,
    "December": 31
}

n = input("Enter a name of month: ")

if n in months:
    print("There are {} days in {}".format(months[n], n))
