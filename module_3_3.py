# функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b='25')
print_params(c=[1, 2, 3])

# распаковка параметров
values_list = [5, False, 'текст']
values_dict = {'a': 'слово', 'b': '7', 'c': 4.5}
print_params(*values_list)
print_params(**values_dict)

# распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
