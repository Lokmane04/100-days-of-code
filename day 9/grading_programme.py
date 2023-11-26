students_score = {
  "Lokmane":99,
  "Harris":82,
  "Eimane":91,
  "Kimberly":40,
  "Joseph":65,
  "Jane":90,
  "Joshua":100,
}
students_grades = {}
for key in students_score:
  score_value=students_score[key]
  if score_value > 90:
     students_grades[key]= "Outstanding"
  elif score_value>80:
    students_grades[key] = "Exceeds Expectations"
  elif score_value>70:
    students_grades[key] = "Acceptable"
  elif score_value>60:
    students_grades[key] = "Fail"

print(students_grades)