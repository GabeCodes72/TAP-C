import math

shifttime = int(input("How many hours do you work per day? > "))
wage = int(input("How much do you make per hour? > $"))
income = shifttime*wage
goal = int(input("How much do you want to save up? > $"))
saved = int(input("How much do you have saved? $"))

mtg = goal-saved

ttg = int(mtg)/int(income)
day = round(ttg, -1)
week = round(ttg/7, -1)
month = round(ttg/30, -1)
year = round(ttg/365, -1)
print(f"It will take about {day} days,")
print(f"{week} weeks, {month} months, or {year} years")
print("to earn that on your current salary.")

input("Thank you for using the TAP-C. Please press enter to exit the program.")