#FutureTime.py
#Name: Aurora Gunubu
#Date: 2/2/25
#Assignment: Lab #2 - FutureTime

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  moreHrs = int(input("Input number of hours\n"))
  moreMins = int(input("Input number of minutes\n"))
  extraHour = (currentMinute + moreMins) // 60

  futureMins = (currentMinute + moreMins) % 60
  futureHour = (currentHour + moreHrs + extraHour)
  futureHour = ((futureHour - 1) % 12) + 1
  
  print(f"{futureHour:02}:{futureMins:02}")

# Just learned how to use brackets for this assignment.
# Changed current hour to -6 to match CST.


if __name__ == '__main__':
  main()
