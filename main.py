def password_read():
    try:
        password = input("Please enter your password to encode: ")
        val = int(password)
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


def decode(password): # my partner implemented
    password_decoded = ''
    for i in password:
        i_add = int(i) + 7
        i_mod = i_add % 10
        password_decoded = password_decoded + str(i_mod)
    return password_decoded
    pass


def display_menu():  # this is the Menu display
    print('\nMenu\n'
          "-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def menu_option():
    try:
        display_menu()
        return int(input("Please enter an option: "))
    except ValueError:
        return -1 #Invalid



def main(): # the function
    password = ""

    while True:

        option = menu_option()

        if option == 1: # Encode
            password = encode(password_read())
            print("Your password has been encoded and stored!")

        elif option == 2: # Decode

            print(f"The encoded password is {password},and the original password is {decode(password)}.")

        elif option == 3: # Quit
            break

if __name__ == '__main__':
    main()
