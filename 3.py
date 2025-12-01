#Варіант 2
#• Реалізуйте ітератор для обходу елементів списку у зворотному порядку.
#• Створіть генератор, який генерує всі парні числа від 2 до N.
#• Зробіть генератор, який видає всі слова з рядка довжиною більше 3 символів.

def reverse_iterator(lst):
    for i in range(len(lst)-1, -1, -1):
        yield lst[i]

print(list(reverse_iterator([1, 2, 3, 4, 5])))


def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i

print(list(even_numbers(10)))


def long_words(s):
    for word in s.split():
        if len(word) > 3:
            yield word

print(list(long_words("це приклад рядка з довгими словами")))
