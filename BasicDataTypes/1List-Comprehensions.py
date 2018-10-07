



def printList(x, y, z, n):
    lst = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if( i+ j + k != n)]
    print(lst)

def main():
     x = int(input())
     y = int(input())
     z = int(input())

     n = int(input())

     printList(x, y, z, n)



if __name__ == '__main__':
    main()
    