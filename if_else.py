"""If else statements are used to carry 
conditional executions
Here, we see a program to check sign of a number"""
def main():
    num = int(input("Enter a number: "))
    if num == 0:
        print("Your number is 0. ")
    else:
        if num > 0:
            print("Your number is positive. ")
        else:
            print("Your number is negative. ")

if __name__ == '__main__':
    main()
