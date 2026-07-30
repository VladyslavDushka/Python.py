import random

def get_valid_input(user_input):
    while True:
        try:
            value = int(input(user_input))
            if value < 0:
                raise ValueError("Invalid input")
            return value
        except ValueError as e:
            print(f"error: {e}")

def check_professor_consistancy(student_count):
    student_scores = []
    for _ in range(student_count):
        student_scores.append((random.randint(50,100), random.choice([True, False])))

    print("\nStudent scores:")
    for i, (score,result) in enumerate(student_scores, 1):
        status = "Passed" if result else "Failed"
        print(f"Student {i}:\tscore = {score}\tresult = {status}")

    passing_scores = [score for score, result in student_scores if result]
    failing_scores = [score for score, result in student_scores if not result]

    min_passing_score = min(passing_scores) if passing_scores else 100
    max_failing_score = max(failing_scores) if failing_scores else 49

    print("-" * 25)
    if min_passing_score <= max_failing_score:
        print("Professor isnt consistancy.")
        print(f"There is a student who passed with a score of {min_passing_score},"
              f"but there is a student who failed with a score of {max_failing_score}")
    else:
        print("Professor is consistancy.")
        threshold_start = max_failing_score + 1
        threshold_end = min_passing_score
        print(f"the threshold for passing the exam is in range of {threshold_start} - {threshold_end} points")

student_count = get_valid_input(f"How many students do you have? ")
check_professor_consistancy(student_count)

