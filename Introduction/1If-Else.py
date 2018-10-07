
#Python If-Else


def inInclusiveRange(x, a, b):

    if x in range(a, b):
        return True
    elif x == b:
        return True
    else :
        return False

def isEven(x):
    if x % 2 == 0:    return True
    else:             return False


def main():
    n = int (input("Enter your Number : "))
    if isEven(n):
       if inInclusiveRange(n, 2, 5):    print("Not Weird")
       elif inInclusiveRange(n, 6, 20): print ("Weird")
       else:                            print ("Not Weird")    
    else:
        print("Weird")







if __name__ == '__main__':
    main()
    