alphabets = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]

print("Welcome to caesar cipher game where we shift your message to specific number!")

while True:
    user_choice = input("Choose between enc for encryption and dec for decryption: ").lower()
    if user_choice not in ["enc", "dec"]:
        print("Not in the choices!")
    else:
        print("Good we'll proceed to next step")
        break

while user_choice == "enc":
    shifted_number = input("Provide number for the msg to shift: ")
    if not shifted_number.isdigit():
        print("Numerical only!")
    else:
        print("Nice!")
        break
else:
    dec_message = input("Input the message you want to decrypt: ")
    while True:
        if dec_message.isdigit():
            print("Digit isn't allowed! ")
            dec_message = input("Input the message you want to decrypt: ")
        else:
            break