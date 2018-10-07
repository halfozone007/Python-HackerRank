


def generateNumbers(n):

    i = 1
    while i <= n :
        yield i
        i += 1

def printNumbers(n):

    for x in generateNumbers(n):
        print(x, end="")   

def main():
    n = int(input("Enter the Number : "))

    printNumbers(n)

if __name__ == '__main__':
    main()
    