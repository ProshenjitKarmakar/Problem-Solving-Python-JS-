if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    result = 0
    item = 0
    for mark in marks :
        result += mark
        item += 1
    
    avg = result/item
    formatted_number = "{:.2f}".format(avg)

    print(formatted_number)





