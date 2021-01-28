def main():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Factorial for negative numbers do not exist. ")
    elif num == 0:
        print("The required factorial is 1. ")
    else:
        print("The required factorial of " + str(num) + " is", factorial(num))  #call a function


def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num - 1)


if __name__ == '__main__':
        main()
