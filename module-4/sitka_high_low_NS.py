# Imported sys for sys.exit
import sys
import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and temperatures from this file. Added lows list and TMIN data.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Introduction and UI
print("Welcome to Weatherly! Please input 'Highs' for the high temperatures and 'Lows' for the low temperatures."
      " If you would like to leave, please input 'Exit' to exit.")
while True:
    choice = input("Please enter your selection: ").strip().capitalize()
    if choice == "Highs":
        # Plot the high temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == "Lows":
        # Plot the low temperatures.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    elif choice == "Exit":
        # Option to exit program
        print("Goodbye!")
        sys.exit()
    else:
        # Notify user of invalid input
        print("Please enter 'Highs', 'Lows', or 'Exit' to exit.")