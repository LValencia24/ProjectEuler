# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


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