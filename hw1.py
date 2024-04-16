# strings


#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

fruits = 'melo918n ora34nge appl1234'

founder = [n for n in fruits if n.isdigit()]

print(','.join(founder))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі


letter = 'hel00 2 f123om L6iv d3341r'

founder = (',  '.join(''.join(words if words.isdigit() else ' ' for words in letter).split()))
res = ' '.join(founder)

print(res)

# list comprehension


# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
l = [w for w in greeting.upper()]

print(l)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

nums = [i ** 2 for i in range(51) if i % 2 != 0]
print(nums)


# function
#


# - створити функцію яка виводить ліст
def li(list):
    print(list)


li([11, 22, 33, 44, 55, 66, 77, 88, 99])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def three(a, b, c):
    max_num = max(a, b, c)
    print(max_num)
    return max_num


three(100, 50, 200)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def gow(*args):
    min_num = min(args)
    print(max(args))
    return min_num


gow(12, -1, 32, -100, 199)

# - створити функцію яка повертає найбільше число з ліста

ranked = [11, -1, 2133, -9, 7]


def the_bigest(ranked):
    max_num = max(ranked)
    print(max_num)
    return max_num


the_bigest(ranked)

# - створити функцію яка повертає найменьше число з ліста

nums = [-12, -21, -31, 1, 0, -24]


def less(nums):
    min_num = min(nums)
    print(min_num)
    return min_num


less(nums)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

age = [11, 15, 19, 7, 23, 45]


def summer(age):
    sum_up = sum(age)
    print(sum_up)


summer(age)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

nums = [12, 21, 5, 52]


def diler(nums):
    average = sum(nums) / len(nums)
    print(average)


diler(nums)

########################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]


listen = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]



#   - знайти мін число
print(min(listen))


#   - видалити усі дублікати

print(set(listen))


#   - замінити кожне 4-те значення на 'X'

print(['x' if not (i + 1) % 4 else item for i, item in enumerate(listen)])


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції



