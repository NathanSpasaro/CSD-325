#program that converts miles to kilometers

def main():
    #display the intro screen
    intro()

    #loop for conversions
    while True:
        get_miles()

        repeat = input("Would you like to perform another conversion? (Y/N): ").upper()
        if repeat != "Y":
            print("Farewell traveler!")
            break

#the intro function displays an introductory screen
def intro():
    print("Hello traveler!")
    print("Welcome to my conversion center!")
    print("Right now, this program only converts miles to kilometers...")
    print()

#get miles from user
def get_miles():
    #loop for correct input
    while True:
        try:
            miles_needed = int(input("Enter the number of miles you would like to convert: "))

            if miles_needed < 0:
                print("Do not enter negative numbers! Try again!")
                continue
            elif miles_needed == 0:
                print("Zero converts to zero... Try again...")
                continue
            #i am passing up on my gaming time to add easter eggs about the sun...
            elif miles_needed == 93000000:
                print("Are you planning on going to the sun?")
            miles_to_km(miles_needed)
            break #exits the loop
        except ValueError:
            print("Please enter a number!")


#equation for miles to kilometers
def miles_to_km(miles):
    kilometers = miles * 1.60934
    print(miles, "miles converts to", kilometers, "kilometers.")

    #call the main function
main()