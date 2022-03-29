def sum_two_smallest_numbers(numbers):
    minimo = min(numbers)
    temp=numbers[0]

    for i in range(len(numbers)):
        if temp==minimo:
            temp=numbers[i+1]
        elif minimo == numbers[i]:
            continue
        elif numbers[i] < temp:
            temp= numbers[i]

    return minimo + temp


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))