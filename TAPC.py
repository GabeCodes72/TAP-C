shifttime = int(input("Hours per Day > "))
wage = int(input("Money per Hour > $"))
income = shifttime*wage
goal = int(input("Goal > $"))
saved = int(input("Current Money Saved > $"))

mtg = goal-saved

ttg = int(mtg)/int(income)
day = ttg//1
week = ttg//7
month = ttg//30
year = ttg//365

def aot():
  if 0 <= ttg <= 6:
  		print(f"It will take about {day} day(s) to reach your goal")
  elif 7 <= ttg <= 29:
  		print(f"It will take about {week} week(s) to reach your goal.")
  elif 30 <= ttg <= 364:
    	print(f"It will take about {month} month(s) to reach your goal.")
  elif ttg >= year:
    	print(f"It will take about {year} year(s) to reach your goal.")
print()
aot()
input("Thank you for using the TAP-C. Please press enter to exit the program.")
