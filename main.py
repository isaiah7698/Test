def main():
    intro()

    try:
        miles = float(input('Enter the number of miles: '))

        miles_to_kilometers(miles)

    except:
        print('An exception occurred, try again by entering only a number')
        print()
        main()

def intro():
    print('This program converts measurements')
    print('In miles to kilometers. For your')
    print("reference the formula is:")
    print('1 miles = 1.60934 kilometers')
    print()

def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    print('That converts to', kilometers,'kilometers')

main()
