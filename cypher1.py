"""

    asks the user for one line of text to encrypt;
    asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
    prints out the encoded text. 
"""

# Input the text you want to encrypt.
text = input("Enter message: ")

# Enter a valid shift value (repeat until it succeeds).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char

print(cipher)
    