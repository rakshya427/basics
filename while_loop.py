"""This program is an example of while loop.
   While loop is used for repeated execution
   as long as the expression is true. While
   loops are useful when the iteration quantity is unknown.
   Here, we add the user input numbers unless -1 is entered.
"""
def main():
    total = 0
    num = int(input("Enter a number: "))
    while num != -1:
        total += num
        num = int(input("Enter a number: "))
    print("The total is " + str(total))


if __name__ == '__main__':
    main()