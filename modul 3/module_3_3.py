def print_params(a=1,b = 'Urban', c = True):
    print(a,b,c)
    
print_params()
print_params(a = 45)
print_params(c = [3,4,5])

values_list = [86, 'Truena', True]
values_dict = {'a': 82,'b': 'skyline', 'c': True}

print_params(*values_list)
print_params(**values_dict)

value_list_2=[False, 12.5]
print_params(*value_list_2, 42)