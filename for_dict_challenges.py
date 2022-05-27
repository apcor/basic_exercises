# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

name_list = []
for student in students:
    name_list.append(student['first_name'])

for name in set(name_list):
    print(f'{name}: {name_list.count(name)}')

# Another option using Collections library
cnt = Counter()
for student in students:
    cnt[student['first_name']] += 1

for name, count in dict(cnt).items():
    print(f'{name}: {count}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_list = []
for student in students:
    name_list.append(student['first_name'])
print(f'The most common student name is {Counter(name_list).most_common(1)[0][0]} \
({Counter(name_list).most_common(1)[0][1]} occurences).')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for group_num, group in enumerate(school_students):
    name_list = []
    for student in group:
        name_list.append(student['first_name'])
    print(f'The most common student name in the class {group_num + 1} is {Counter(name_list).most_common(1)[0][0]} \
({Counter(name_list).most_common(1)[0][1]} occurences).')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for group in school:
    gender_list = []
    for student in group['students']:
        gender_list.append(is_male[student['first_name']])
    print(f"In the class {group['class']} there are \
{gender_list.count(True)} boys and \
{gender_list.count(False)} girls.")



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys = {}
girls = {}
for group in school:
    gender_list = []
    for student in group['students']:
        gender_list.append(is_male[student['first_name']])
    boys[gender_list.count(True)] = group['class']
    girls[gender_list.count(False)] = group['class']
print(boys)
print(girls)
print(f"The class {boys[max(boys)]} has the most boys - {max(boys)}.\n\
The class {girls[max(girls)]} has the most girls - {max(girls)}.")
