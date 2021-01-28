import random


def main():
    print("This program generates a random number ")
    minimum = int(input("Enter a  minimum integer number: "))
    maximum = int(input("Enter a maximum integer number: "))
    number = random.randint(minimum, maximum)
    print("The required random number is ", number)


if __name__=='__main__':
    main()

