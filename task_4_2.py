# Задача 2. Впервой строке файла находится информация об ассортименте мороженного, во второй -информация о том, какое мороженное есть на складе.
#  Выведите названия того товара, который закончился.

data = open('icecream_list.txt', encoding='utf-8')
icecream_all = data.readline()
icecream_rest = data.readline()
data.close()

icecream_all = icecream_all.strip('\n').split(', ')
icecream_rest = icecream_rest.split(', ')

icecream_all = set(icecream_all)
icecream_rest = set(icecream_rest)

no_icecream = icecream_all.difference(icecream_rest)
print(f'Товар, который закончился - {no_icecream}')


