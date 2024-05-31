first = int(input('Ведите число: '))
second = int(input('Ведите число: '))
third = int(input('Ведите число: '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)