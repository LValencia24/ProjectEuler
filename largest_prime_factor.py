def num_prim(number):
    primo = True

    for i in range(2, number):
        if number%i==0:
            primo = False
            break
        else:
            pass

    return primo

def largest_prime_factor(numberMax):
    number_result = numberMax
    prim_max = 0
    
    for i in range(2, numberMax):
        if number_result%i==0 and num_prim(i)==True:
            number_result = number_result / i
            prim_max = i
            if number_result == 1:
                break
            else:
                pass
        else:
            pass

    return prim_max

print(largest_prime_factor(600851475143))

