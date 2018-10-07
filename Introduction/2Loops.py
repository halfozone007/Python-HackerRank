
def returnSquares(n):
    i = 0
    while(i < n):
        yield  (i * i)
        i +=1
  


def main():
    n = int(input("Enter a number : "))


    for x in returnSquares(n):
        print(x)




if __name__ == '__main__':
    main()
    