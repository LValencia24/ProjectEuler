def pythagorean_triplet(number1, number2, number3):
    triplet = True

    if number1 < number2 and number2 < number3:
        if number1 + number2 == number3:
            pass
        else:
            triplet = False
    else:
        triplet = False

    return triplet

k = 0
result = 0

for i in range(1, 1000):
    for j in range(1, 1000):
        k = (i**2 + j**2)**(1/2)
        if pythagorean_triplet(i**2, j**2, k**2) == True and i + j + k == 1000:
            result = i * j * k 
            break
        else:
            pass

print(result)

