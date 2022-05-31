def fizz_buzz(num):
    if type(num) != int:
        return 'Only integer values are allowed'
    elif num % 3 == 0 and num % 5 == 0:
        return 'fizz buzz'
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0:
        return 'fizz'
    else:
        return str(num)
