grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_ = list(students)
list_.sort()

average_1 = sum(grades[0])/len(grades[0])
average_2 = sum(grades[1])/len(grades[1])
average_3 = sum(grades[2])/len(grades[2])
average_4 = sum(grades[3])/len(grades[3])
average_5 = sum(grades[4])/len(grades[4])

students_dict ={list_[0]:average_1, list_[1]:average_2, list_[2]:average_3, list_[3]:average_4, list_[4]:average_5,}
print(students_dict)