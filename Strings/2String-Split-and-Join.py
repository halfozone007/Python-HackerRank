def split_and_join(line):
    splitedStr = line.split(" ")
    joinedStr = "-".join(splitedStr)
    return joinedStr




def main():
    line = input()
    result = split_and_join(line)
    print(result)

if __name__ == '__main__':
    main()
   