def palindrome_number(number):
    palindrome = True

    number_one = str(number)
    number_two = number_one[::-1]

    if number_one == number_two:
        pass
    else:
        palindrome = False

    return palindrome

palindrome_max_one = 0
palindrome_max_two = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        number_multiplicate = i * j
        if palindrome_number(number_multiplicate) == True:
            palindrome_max_one = number_multiplicate
            if palindrome_max_one > palindrome_max_two:
                palindrome_max_two = palindrome_max_one
            else:
                pass
        else:
            pass

print(palindrome_max_two)





