nums = {"one": 1, "two": 2, "three": 3}

# values
for num in nums.values():
    print(num)

# keys
for key in nums.keys():
    print(key)


# keys & values
for item in nums.items():
    print(item)

for k, v in nums.items():
    print(f"k is {k} and value is {v}")


# using 'IN' word
print(2 in nums.values())
print('one' in nums.keys())

'''dictionary methods'''
# CLEAR
d = dict(a=1, b=2, c=3)
#d.clear()
print(d)

#COPY
c = d.copy()
print(c)
print(c is d) # False

#FROMKEYS
x = {}.fromkeys("a", "b")
print(x)
y = {}.fromkeys(['a', 'b', 'c'], 10)
print(y)

#словарь из двух списков с ZIP
keys = ['one', 'two', 'three', 'four']
values = [1,2,3,4]
a = {k: v for k, v in zip(keys, values)}
print(a)

# GET - получает значение по ключу, но не выкидывает KeyError, а None.
print(d['a']) # 1
print(d.get('a')) # 1
print(d['no_key']) # KeyError
print(d.get('no_key')) # None

'''
-- например, там, где надо узнать сколько раз встречается ключ в словаре.
# имеем список 
lst = [9, 13, 1, 3, 7, 3, 1, 1, 7, 1, 7, 9]
# создаем ключи будущего словаря (множество set() 
# может иметь только уникальные элементы)
key = set(lst)
# создаем словарь `rez` из списка ключей `key` 
# со значением по умолчанию = 0
rez = dict.fromkeys(key, 0)
# {1: 0, 3: 0, 7: 0, 9: 0, 13: 0}

for key in lst:
    # увеличиваем счетчик 
    # соответствующего ключа на 1
    rez[key] += 1

# смотрим результат
print(rez)
{1: 4, 3: 2, 7: 3, 9: 2, 13: 1}
'''
