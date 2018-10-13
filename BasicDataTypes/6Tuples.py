


def generateHash(listTuple):
    hashvalue = hash(listTuple)
    return hashvalue


def main():
    n = int(input())
    integer_list = map(int, input().split())

    listTuple = tuple(integer_list)

    result = generateHash(listTuple)
    print(result)


if __name__ == '__main__':
    main()
    