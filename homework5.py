immutable_var = 1, 2, 4, 5, 7, 8, 'long', 'car'
print(immutable_var)
#immutable_var[0] = 0 #Кортеж не поддерживает обращение по элементам, но есть исключения 
#print(immutable_var)

#Исключения 
immutable_var_1 = ([20, 0], 3) + (1, 2)
print(immutable_var_1)
immutable_var_1[0][0] = 10
print(immutable_var_1)
immutable_var_2 = (1, 2) * 3
print(immutable_var_2)

mutable_list = [1, 2, 3, 4, 'Vlad']
print(mutable_list)
mutable_list[4] = 'Urban'
print(mutable_list)