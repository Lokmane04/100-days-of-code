print("----------welcome to the height generator---------")
students_heights = input("Type in the student's heights in cm (eg : 154 163 184 156) : ").split(' ')
average_height:float =0
count = 0
for height in students_heights:
  average_height += int(height)
  count+=1
print(average_height/count)