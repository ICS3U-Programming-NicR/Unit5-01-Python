#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display 5 ints in a line


def fahrenheit():
    while True:
        temp_celc_str = input("Enter the temperature in celcius: ")
        try:
            temp_celc = float(temp_celc_str)
            temp_fahren = ((9 / 5) * temp_celc) + 32
            print("the temperature in farenheit is {}".format(temp_fahren))
        except:
            print("You have to enter a real number")
        input("To run the program again just press <enter>")
    return 0


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
