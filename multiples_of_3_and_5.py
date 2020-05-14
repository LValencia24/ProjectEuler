def sum_of_multiples_numbers(number1, number2, numberMax):
    count = 0

    for i in range(numberMax):
        if i%number1==0 or i%number2==0:
            count += i
        else:
            pass

    return count

print(sum_of_multiples_numbers(3, 5, 1000))