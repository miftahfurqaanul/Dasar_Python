for num in range(1, 20):
    if num > 10:
        break
    is_prime = True
    for div in range(2, num):
        if num % div == 0:
            is_prime = False
            break
    if is_prime:
        print(num)