"""
    Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple – you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

    1 January 2017 = 2017 01 01
    2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
    1 + 2 = 3

3 is the digit we searched for and found.

Your task is to write a program which:

    asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY – actually, the order of the digits doesn't matter)
    outputs the Digit of Life for the date.

"""

date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Your Digit of Life is: " + date)
	