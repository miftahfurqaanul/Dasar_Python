num = 1
while num * num <= 10:
    square = num * num
    if square % 2 == 0:
        print(f"{square} is even")
    else:
        print(f"{square} is odd")
    num += 1