# Author: Colton Jones
# Section: ZA
# Description: simulates student grading

from functools import reduce

def get_student():
    input_student_name = input('Please enter the student\'s name: ')
    input_student_id = input('Please enter the student\'s ID: ')
    return input_student_id, input_student_name

def input_assignments(student, number_of_assignments) -> None:
    scores = []
    print('\n' + f'Please enter the scores for {student["Name"]}')
    for count in range(1, number_of_assignments + 1):
        is_valid = False
        while not is_valid:
            input_grade = input(f'Please enter a grade (0-100) for assignment {count}: ')
            try:
                grade = float(input_grade)
                if grade < 0 or grade > 100:
                    print('Grade must be between 0 and 100.')
                else:
                    scores.append(grade)
                    is_valid = True
            except ValueError:
                print('Please enter a valid grade.')
    student['Scores'] = scores

def grade_student(student) -> None:
    # equivalent of a javascript reduce to easily sum up the scores, then divide them by total number of scores
    student['Average'] = reduce(lambda total, score: total + score, student['Scores']) / len(student['Scores'])

def print_report(students: dict) -> None:
    #assignment_grade_sums = [0]
    output = '\n' + 'Final Grade Report:' + '\n'
    for student in students.values(): # we don't need the key so we just iterate through the list of values
        output += f'{student["Name"]}\'s average score was {student["Average"]}' + '\n' # double quotes because intellisense didn't like single quotes
        #for score in student['Scores']:
            #assignment_grade_sums
    print(output)

def main():
    print('GRADING SIMULATOR 2022')
    all_students = {}
    is_entering_students = True
    while is_entering_students:
        # we need to ensure that id is unique here or we will be getting weird behavior (overwriting prior students)
        id_is_valid = False
        while not id_is_valid:
            student_id, student_name = get_student()
            id_is_valid = all_students.get(student_id) is None # id is only valid if it doesn't already exist in the dictionary
            if not id_is_valid:
                print('This ID already exists! Please try again with a different ID for this student.')
        all_students[student_id] = {'Name': student_name}
        continue_input = input('Enter another student? (Y)es or (N)o: ')
        is_entering_students = continue_input.upper() != 'N' # no longer entering students if the user input is 'N'
    assignment_amt_input = input('How many assignments were given? ')
    is_valid = False
    while not is_valid:
        try:
            assignment_amt = int(assignment_amt_input)
            is_valid = True
        except ValueError:
            print('Please enter the number of assignments (must use digit characters)')
    for student in all_students.values():
        input_assignments(student, assignment_amt)
        grade_student(student)
    print_report(all_students)
    

if __name__ == '__main__':
    main()