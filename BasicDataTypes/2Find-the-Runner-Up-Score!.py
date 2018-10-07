



def runnerUp(varlist):
    varlist.sort(reverse = True)
    maxval = varlist[0]

    i = 1
    length = len(varlist)
    while (varlist[i] == maxval and i < length):
        i+=1
    
    return varlist[i]



def main():
    n = int(input())
    arr = map(int, input().split())
    varlist = list(arr)
    result = runnerUp(varlist)

    print(result)





if __name__ == '__main__':
    main()
    