"""
For loops are used when the number of iterations is unknown.
Here, we print out even numbers.
"""
def main():
    for i in range(10):
        print(i * 2)

    for i in range(0,6,2):
        print(i)

    for num in [2,4,6,8]:   #for each loop
        print(num)


if __name__ == '__main__':
        main()