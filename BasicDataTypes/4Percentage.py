


def calculatePercentage(query_name, student_marks):
    
    marks = student_marks[query_name]
    
    total = 0
    for x in marks:
        total += x
    
    percentage = total/3
    return percentage
    




def main():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = calculatePercentage(query_name, student_marks)
    print ("{0:.2f}".format(result))


if __name__ == '__main__':
    main()
    