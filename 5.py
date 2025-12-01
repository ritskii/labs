#Варіант 2
#• Об’єднайте два списки назв та цін за допомогою zip() у словник.
#• Підрахуйте середню ціну товарів через reduce().

from functools import reduce

def products_dict(names, prices):
    return dict(zip(names, prices))

print(products_dict(["яблуко", "банан", "груша"], [10, 20, 30]))


def average_price(prices):
    return reduce(lambda a, b: a + b, prices) / len(prices)

print(average_price([10, 20, 30]))
