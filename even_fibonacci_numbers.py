def es_par(number):
    esPar = True
    if number%2==0:
        pass
    else:
        esPar = False

    return esPar

def sum_of_fibonacci_number(numberMax):
    count = 0
    a = 1
    b = 2

    while True:
        if es_par(a)==True:
            count += a
        if es_par(b)==True:
            count += b

        a = a + b
        b = b + a

        if a > numberMax:
            break
        elif b > numberMax:
            break
        else:
            pass

    return count
    
print(sum_of_fibonacci_number(4000000))
