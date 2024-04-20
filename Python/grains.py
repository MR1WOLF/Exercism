from math import pow
def square(number):
    """This function calculates the number of grains on a given square
    :param, int (number) - the index of the square
    :return: the number of grains
    """
    if(number > 64 or number < 1):
        raise ValueError("square must be between 1 and 64")
    return int(pow(2,number - 1)) 


def total():
    sum = 0
    for i in range(1,65):
        sum += pow(2,i-1)
    return int(sum)-1       # Here we substitute one because we want to avoide counting the first chess board twice !

