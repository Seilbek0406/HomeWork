current_scores = [85, 90, 78, 92] 
module1_scores = [80, 85, 75, 88] 
module2_scores = [78, 82, 70, 85] 
session_scores = [90, 88, 85, 80]

def calculate_final_grade(current, module1, module2, session):
    module_average = (module1 + module2) / 2
    grade = (current * 0.4) + (module_average * 0.2) + (session * 0.4)
    return grade

final_grades = []
for i in range(len(current_scores)):
    final_grade = calculate_final_grade(current_scores[i], module1_scores[i], module2_scores[i], session_scores[i])
    final_grades.append(final_grade)

for i, grade in enumerate(final_grades):
    print(f"Студент {i + 1}: итоговая оценка за семестр = {grade:.2f}")
