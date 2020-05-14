def sum_of_square(number):
    sum_square = 0

    for i in range(1, number+1):
        sum_square += i**2

    return sum_square

def square_of_sum(number):
    square_sum = 0
    square_sum_total = 0

    for i in range(1, number+1):
        square_sum += i

    square_sum_total = square_sum**2

    return square_sum_total

total = 0

total = square_of_sum(100) - sum_of_square(100)

print(total)
