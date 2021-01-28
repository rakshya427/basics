def main():
    num = int(input("Enter a number: "))
    if num == 1:
        print(" 1 is neither prime nor a composite number. ")
    elif num == 0:
        print("0 is not a prime number. ")
    elif num == 2:
        print("2 is a prime number. ")
    elif num > 2:
        for i in range(2, num//2):
            if (num % i) == 0:
                print(num, "is not a prime number. ")
        else:
            print(num, "is a prime number. ")


if __name__ == '__main__':
    main()
