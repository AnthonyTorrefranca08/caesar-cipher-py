alphabets = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]

print("Welcome to Caesar Cipher where we'll encrypt a message for you")
while True:
    shift_number = input("Input a number for your message to shift! ")
    if not shift_number.isdigit():
        print("Pls enter a valid number")
    else:
        break
while True:
    en_or_dec = input("Type 'Enc' to Encrypt or 'Dec' to decrypt: ").lower()
    if en_or_dec not in ['enc', 'dec']:
        print("Uh oh try again:")
    else:
        print("Next we'll proceed with the msg")
        break
while True:
    msg = input("The message! ").lower()

    print(msg)