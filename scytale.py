import pyfiglet
from math import ceil

def scytale_process(input, diameter):
    out = str()

    for y in range(0,diameter):
        out += input[y::diameter]
    return out

def scytale_init(input, diameter, mode):
    input = str(input)
    if mode == 1:
        diameter = ceil(len(input)/diameter)
    return scytale_process(input, diameter)


def main_menu(user_input, menu):
    mode = ["encoded", "decoded"]

    while True:
        print(menu)
        try:
            user_input = int(input("Enter your selection:[0] \n"))
        except: 
            user_input = 0
        
        if user_input == 2:
            break
        elif user_input in [0,1]:
            user_string = str(input(f"\nPlease enter a string to be {mode[user_input]}: \n"))
            try:
                user_diameter = int(input("\nPlease enter a diameter:[2] \n"))
            except:
                user_diameter = 2
            print(f"\nYour {mode[user_input]} string:\n" + scytale_init(user_string, user_diameter, user_input) + "\n")


def welcome_user():
    entry_banner = pyfiglet.figlet_format("Scytale", font='isometric1')
    menu = """What do you wanna do?\n
    [0] Encode a given string (default)\n
    [1] Decode a given string\n
    [2] I wanna go to Rio (exit)\n"""

    print(entry_banner)
    main_menu(0, menu)
    return print(pyfiglet.figlet_format("\nCya next time! Bye!",font='digital'))
        
if __name__ == '__main__':
    welcome_user()
