my_dict = {'Vlad': 2004, 'Kostay' : 2004, 'Valera': 2003}
print('Дикт:',my_dict)
print('Существующее значение:', my_dict.get('Kostay'))
print('Не существующее значение:', my_dict.get('Voloday'))
my_dict.update({'Vova': 2002, 'Vasya':1999})
a = my_dict.pop('Valera')
print('Удаленное значение:', a)
print('Модифицированный словарь:', my_dict, end ='\n\n')

my_set = {2024, 'Urban', 27 , 5}
print('Набор:',my_set)
my_set.update({1999,2004})
my_set.discard(5)
print('Модифицированный набор:', my_set)