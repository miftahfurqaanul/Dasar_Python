numbers = [41, 5, 1, 3, 89, 32]

for i  in range(len(numbers)):
    for j in  range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)
