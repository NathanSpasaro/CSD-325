# Nathan Spasaro
# 09/06/2026
# Assignment 1.2
# Purpose: Count down bottles of beer from a user-entered number and display the song lyrics.

# Function that manages the bottle countdown.
def beer_countdown(bottles):
    for i in range(bottles, 0, -1):

            # Handle the final countdown with correct verbiage.
            if i == 1:
                print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
                print("Take one down, pass it around, no more bottles of beer on the wall.")

            # Handle two bottles for the next line to correctly state "1 bottle."
            elif i == 2:
                print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
                print(f"Take one down, pass it around, {i -1} bottle of beer on the wall.")

            # Handle all other countdowns.
            else:
                print (f"{i} bottles of beer on the wall, {i} bottles of beer.")
                print (f"Take one down, pass it around, {i -1} bottles of beer on the wall.")

            print()

# Get and validate number of starting bottles.
while True:
    try:
        bottles = int(input("How many bottles are on the wall? "))

        if bottles <= 0:
            print("Please enter a positive integer.")
            continue

        break

    except ValueError:
        print("Please enter a positive integer.")

# Pass the user's input to the countdown function
beer_countdown(bottles)

# Return to the main program and remind the user to buy more beer.
print("Time to buy more beer!")