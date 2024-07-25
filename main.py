def password_read():
    try:
        password = int(input("Please enter your password to encode: "))
        return str(password)
    except ValueError:
        print("Please enter a valid password.")
        return password_read()


def encode(password): # my implemented
    password_encoded = ''
    for i in password:
        i_add = int(i)+3
        i_mod = i_add % 10
        password_encoded = password_encoded + str(i_mod)
    return password_encoded
    pass


def decode(): # my partner implemented
    pass


def display_menu():  # this is the Menu display
    print('\nMenu\n'
          "-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main(): # the function
    password = ""

    while True:
        display_menu()

        option = int(input("Enter your choice: "))

        if option == 1: # Encode
            password = encode(password_read())
            print("Your password has been encoded and stored!")

        elif option == 2: # Decode

            print(f"The encoded password is ----,and the original password is ----.")

        elif option == 3: # Quit
            break

if __name__ == '__main__':
    main()
