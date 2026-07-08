# Encryption Function
def encrypt(text, shift):

    encrypted_text = ""

    for char in text:

        # Checking whether character is alphabet
        if char.isalpha():

            # For uppercase letters
            if char.isupper():
                base = ord('A')

            # For lowercase letters
            else:
                base = ord('a')


            # Caesar Cipher Formula
            encrypted_text += chr(
                (ord(char) - base + shift) % 26 + base
            )


        # Numbers, spaces and symbols remain same
        else:
            encrypted_text += char


    return encrypted_text



# Decryption Function
def decrypt(text, shift):

    decrypted_text = ""

    for char in text:


        if char.isalpha():

            if char.isupper():
                base = ord('A')

            else:
                base = ord('a')


            # Reverse Caesar Cipher Formula
            decrypted_text += chr(
                (ord(char) - base - shift) % 26 + base
            )


        else:
            decrypted_text += char


    return decrypted_text

while True:

    print("\nChoose an option:")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")


    choice = input("\nEnter your choice: ")



    # Encryption

    if choice == "1":

        message = input("\nEnter your message: ")

        shift = int(input("Enter shift key: "))


        encrypted = encrypt(message, shift)


        print("\nEncrypted Message:")
        print(encrypted)



        # Save encrypted message

        file = open("encrypted_message.txt", "w")

        file.write(encrypted)

        file.close()


        print("\nMessage saved to encrypted_message.txt")




    # Decryption

    elif choice == "2":


        message = input("\nEnter encrypted message: ")

        shift = int(input("Enter shift key: "))


        decrypted = decrypt(message, shift)


        print("\nDecrypted Message:")
        print(decrypted)


    # Exit

    elif choice == "3":

        print("\nThank you for using Encryption Tool")
        break

    else:

        print("\nInvalid Option! Try again.")