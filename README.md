# Lab9_Software-Engineering
def encode(password): # my implemented
    pass


def decode(): # my partner implemented
    pass


def display_menu():
    print('\nMenu\n'
          "-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main():
    while True:
        display_menu()
        option_menu = print("Please enter an option: ")
        if option_menu == 1:
            print("Encode")

        elif option_menu == 2:
            print("Decode")

        elif option_menu == 3:
            break

if __name__ == '__main__':
    main()
