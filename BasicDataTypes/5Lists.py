

def performOperations(varList):
  
    resultList = list()
  
    for x in varList:  
        #split the the list
        # ['insert' 1 6] becomes [insert][1][6]  
        y = x[0].split()
       
        if y[0] == "insert": 
            pos = int(y[1])      
            val = int(y[2])              
            resultList.insert(pos, val)
        elif y[0] == "print":        
            print(resultList)
        elif y[0] == "remove":
           
            val = int(y[1])
            resultList.remove(val)
        elif y[0] == "append":
           
            val = int(y[1])
            resultList.append(val)
        elif y[0] == "sort":
          
            resultList.sort()
        elif y[0] == "pop":
           
            resultList.pop()
        elif y[0] == "reverse":
            
            resultList.reverse()




def readData():

    n = int(input())

    #creat the list to read the data
    inputdataList = list()

    while n > 0:
        str = input()

        #create a sublist to store individual commands
        sublist = list()
        
        sublist.append(str)     
        if str == "insert":           
            pos = int(input())
            val = int(input())           
            sublist.append(pos)
            sublist.append(val)
                
        elif str == "append":
            val = int(input())          
            sublist.append(val)

        elif str == "remove":
            val = int(input())         
            sublist.append(val)
        
        n -= 1
        inputdataList.append(sublist)
    
    return inputdataList

    



       
           
             

            
            

def main():
    
    #read the data 
    varlist = readData()
    
    #perform the operations
    performOperations(varlist)



if __name__ == '__main__':
    main()
    