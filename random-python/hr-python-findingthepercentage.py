if __name__ == '__main__':
    student_marks = {"Malika": [52, 56, 60]}
    query_name = "Malika"
    sum = 0
    for i in student_marks[query_name]:
        sum += i
    score = sum/len(student_marks[query_name])
    print("%.2f" % score)
