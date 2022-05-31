# def factorial(num):
#     result = 1
#
#     for i in range(1, num+1):
#         result *= i
#
#     return result

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

print(factorial(3))

def sum_series(nth, first = 0, second = 1):
    pass

sum_series(6)
sum_series(6, 2, 1)
sum_series(6, 5, 2)