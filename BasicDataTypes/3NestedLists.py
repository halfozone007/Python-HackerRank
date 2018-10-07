



def secondLowestGrade(varlist):
   
   #sorting the list based on the score
   varlist.sort(key = lambda x : x[1])

   length = len(varlist)
   lowestVal = varlist[0][1]
   i = 0
   nameList = list()
   
   #skip through the lowest val sublist
   while (i < length and varlist[i][1] == lowestVal):
        i+=1
   
   secondLowestVal = varlist[i][1]
   #Add the second lowest val names in the list
   while (i < length and varlist[i][1] == secondLowestVal ):
        nameList.append(varlist[i][0])
        i += 1
   
   nameList.sort()
   return nameList

def main():
    varlist = list()
    for _ in range(int(input())):
        sublist = list()
        name = input()
        score = float(input())
        sublist.append(name)
        sublist.append(score)
        varlist.append(sublist)
    
    resultNameList = secondLowestGrade(varlist)

    for name in resultNameList:
        print(name)




if __name__ == '__main__':
    main()
    