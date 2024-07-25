# it works


def encode(password): # my implemented

    pass


def decode(): # my partner implemented
    pass


password = 0

def display_menu():  # this is the Menu display
    print('\nMenu\n'
          "-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main(): # the function

    while True:
        display_menu()
        option_menu = int(input("Please enter an option: "))

        if option_menu == 1: # Encode
            password_encode = int(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        elif option_menu == 2: # Decode

            print(f"The encoded password is ----,and the original password is ----.")

        elif option_menu == 3: # Quit
            break

if __name__ == '__main__':
    main()


