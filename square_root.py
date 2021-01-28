import math


def main():
    print("This program calculates the square root")
    num = int(input("Enter a positive number"))
    if num == 1:
        print("The square root is 1. ")
    elif num == 0:
        print(" The square root is 0. ")
    elif num > 0:
        square_root = math.sqrt(num)
        print("The square root of " + str(num) + " is", square_root)


if __name__ == '__main__':
    main()

