#This program calculates the amount of days elapsed between two dates
#Paul Ireland 21/01/2020

xmas_day = 25
xmas_month = 12
xmas_year = 2020

born_day = input("Enter the day that you were born (1-31): ")
born_month = input("Enter the number of the month that you were born in e.g January = 1 - December = 12: ")
born_year = input("Enter the year that you were born in e.g 1995: ")

born_day = int(born_day)
born_month = int(born_month)
born_year = int(born_year)

print("")

now_day = input("Enter the day today (1-31): ")
now_month = input("Enter todays month e.g. January = 1 = December = 12: ")
now_year = input("Enter todays year e.g. 2018: ")

now_day = int(now_day)
now_month = int(now_month)
now_year = int(now_year)

print("")

years_indays = (now_year - born_year) * 365.25
months_indays = (now_month - born_month) * 30.4 + now_day - born_day
days_born = years_indays + months_indays


print("Approximately",round(days_born), "days have elapsed since your birthday!")

xmas_day = int(xmas_day)
xmas_month = int(xmas_month)
xmas_year = int(xmas_year)

years_indays = (xmas_year - now_year) * 365.25
months_indays = (xmas_month - now_month) * 30.4 + xmas_day - now_day

days_toxmas = years_indays + months_indays

print("and it is only",round(days_toxmas), "days to xmas!")
