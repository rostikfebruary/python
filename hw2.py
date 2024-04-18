# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи

def notebook():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo = todo_list.append(todo)

    def get_all():
        nonlocal todo_list
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()
print(get_all())
add_todo('Vitalik perevir 1 dz bud laksa')
print(get_all())
add_todo('buy beer')
add_todo('watch a movie')
add_todo('learn python')
add_todo('take a shower')
add_todo('get sleep')
print(get_all())
add_todo('get sleep')
print(get_all())




# 2) протипізувати перше завдання
from typing import Optional, Any

MyType = str | int | list


def notebook() -> Optional[MyType]:
    todo_list = []

    def add_todo(todo: str):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list:
        nonlocal todo_list
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()
print(get_all())
add_todo('Vitalik perevir 1 dz bud laksa')
print(get_all())




# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

numbers = lambda num: '+'.join([num + '0' * index for index, num in enumerate(str(num)[::-1]) if num != 0][::-1])

print(numbers(123))



# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

def counter(func):
    count = 0

    def inner_count():
        nonlocal count
        count += 1
        print('Це твій', count, 'виклик')
        func()

    return inner_count


def decor(func):
    def inner():
        print('*' * 22)
        func()
        print('*' * 22)

    return inner


@counter
@decor
def notification():
    print('It`s your notification')


notification()
notification()
notification()
notification()
notification()
