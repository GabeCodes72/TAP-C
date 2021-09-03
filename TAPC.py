import math

shifttime = int(input("Hours per Day > "))
wage = int(input("Money per Hour > $"))
income = shifttime*wage
goal = int(input("Goal > $"))
saved = int(input("Current Money Saved > $"))

mtg = goal-saved

ttg = int(mtg)/int(income)
day = round(ttg, 0)
week = round(ttg/7, 0)
month = round(ttg/30, 0)
year = round(ttg/365, 0)

def aot():
  if 0 <= ttg <= 6:
    print(f"It will take about {day} days to reach your goal")
  elif 7 <= ttg <= 29:
    print(f"It will take about {week} weeks to reach your goal.")
  elif 30 <= ttg <= 364:
    print(f"It will take about {month} months to reach your goal.")
  elif ttg >= year:
    print(f"It will take about {year} years to reach your goal.")
print()
aot()
input("Thank you for using the TAP-C. Please press enter to exit the program.")
