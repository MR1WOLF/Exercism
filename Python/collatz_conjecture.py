def steps(number):
    if(number <= 0):
        raise ValueError("Only positive integers are allowed")
    n = number
    counter = 0
    while(n != 1):
        if (n % 2 == 0): # Even number
            n = n / 2
        else:
            n = 3 * n + 1
        counter+=1
    return counter