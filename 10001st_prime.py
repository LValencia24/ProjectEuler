def num_prim(number):
    primo = True

    for i in range(2, number):
        if number%i==0:
            primo = False
            break
        else:
            pass

    return primo

prime_number = 0
i=1

while prime_number < 10001:
    i += 1
    if num_prim(i)==True:
        prime_number += 1
        print(prime_number)
    else:
        pass

print(i)