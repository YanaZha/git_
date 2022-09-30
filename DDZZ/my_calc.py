def sum_it(x,y):
    return x +y



def difference_it(x,y):
    return x -y


def mult_it(x,y):
    return x * y


def div_it(x, y):
    try:
        return x /y
    except ValueError:
        print('That was no valid number. Try again...')
