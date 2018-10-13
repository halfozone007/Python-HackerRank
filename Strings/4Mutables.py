

#string is a immutable obj
#list is a mutable object

def mutate_string(string, position, character):
    
    new_string = string[:position] + character + string[position+1:]
    return new_string



def main():
    oldstring = input()
    pos, character = input().split()
    result = mutate_string(oldstring, int(pos), character)
    print(result)
   

if __name__ == '__main__':
    main()
    