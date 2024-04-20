from math import pow
def is_armstrong_number(number):
    sum = 0
    length = 0
    original = number
    while number > 0:   # Count the number of digits or Length of the number
        length += 1
        number //= 10
    number = original
    while(number > 0):       # Get the Sum of all digits raised to length of the number
        digit = number % 10
        sum += int(pow(digit,length))
        number //= 10
    return sum == original
print(is_armstrong_number(15))