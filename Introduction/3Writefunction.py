

def isDividedBy4(n):
    if n % 4 == 0 : return True
    else          : return False


def isDividedBy100(n):
    if n % 100 == 0 : return True
    else            : return False


def isDividedBy400(n):
    if n % 400 == 0 : return True
    else            : return False


def isLeapYear(n):
    divisibleBy4 = isDividedBy4(n)
    divisibleBy100 = isDividedBy100(n)
    divisibleBy400 = isDividedBy400(n)

    if divisibleBy4:
        if divisibleBy100:
            if divisibleBy400 :return True
            else              :return False
        else                  :return True
    else                      :return False
    
  




def main():

    n = int(input("Enter the Year :"))

    isleapYear = isLeapYear(n)

    print(isleapYear)



if __name__ == '__main__':
    main()
    