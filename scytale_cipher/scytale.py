#! /usr/bin/env python

from math import ceil


def scytale_process(input: str, diameter: int) -> str:
    """
    process encoding or decoding of a string.

    :input: user input string
    :diameter: user diameter or default

    :returns: with scytale encoded string

    """
    out = str()

    for y in range(0, diameter):
        out += input[y::diameter]
    return out


def scytale_init(input: str, diameter: int, mode: int) -> str:
    """
    prepare process of scytale mode

    :input: user input string
    :diameter: user diameter or default
    :mode: bool to predict if input has to be encoded or decoded

    :returns: encoded or decoded string

    """
    input = str(input)
    if diameter < 1:
        raise ValueError("diameter must be at least 1")
    if mode == 1:
        # decoding path
        n = len(input)
        rows = ceil(n / diameter)
        remainder = n % diameter
        if remainder == 0:
            remainder = diameter

        columns = []
        index = 0
        for col in range(diameter):
            length = rows if col < remainder else rows - 1
            columns.append(input[index:index + length])
            index += length

        out = ""
        for row in range(rows):
            for col in range(diameter):
                if row < len(columns[col]):
                    out += columns[col][row]
        return out

    return scytale_process(input, diameter)


def main_menu(menu: str) -> None:
    """
    enters the cli-wizard menu loop

    :menu: menu prompt string

    """
    mode = ["encoded", "decoded"]

    while True:
        print(menu)
        user_input = input("Enter your selection:[0] \n")
        try:
            user_input = int(user_input)
        except ValueError:
            if user_input not in ["", "0"]:
                print(
                    f"\n'{user_input}' is not a number. Continuing with 0.\n")
            user_input = 0

        if user_input == 2:
            break
        elif user_input not in [0, 1]:
            print(f"\n'{user_input}' is not a valid entry. Try again!\n")
        else:
            user_string = str(
                input(f"\nPlease enter a string to be {mode[user_input]}: \n"))
            user_diameter = input("\nPlease enter a diameter:[2] \n")
            try:
                user_diameter = int(user_diameter)
                if user_diameter < 1:
                    raise ValueError
            except ValueError:
                if user_diameter not in ["", "2"]:
                    print(
                        f"\n'{user_diameter}' is not a valid diameter. Continuing with 2.\n"
                    )
                user_diameter = 2
            print(f"\nYour {mode[user_input]} string:\n '" +
                  scytale_init(user_string, user_diameter, user_input) + "'\n")


def menu_entries() -> str:
    menu = """What do you wanna do?\n
    [0] Encode a given string (default)\n
    [1] Decode a given string\n
    [2] I wanna go to Rio (exit)\n"""

    return menu


def main() -> None:
    menu = menu_entries()
    main_menu(menu)
    print("\nCya next time! Bye!")


if __name__ == '__main__':
    main()
