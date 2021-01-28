def main():
    num = int(input("Enter a number: "))
    if num < 0:   # user should enter a positive number
        print("You entered a negative number")
        print("Please enter a positive number")
    else:
        summation = 0
        summation = (num * (num + 1)) / 2
        print("The required sum of natural numbers is ", summation)




if __name__=='__main__':
    main()

