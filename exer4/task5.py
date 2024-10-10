# 26 13 40 20 10 5 16 8 4 2 1
num = 6
hasil_sequence = [num]
while num != 1:
    if num % 2 == 0:
        num = num // 2 #13
    else:
         num = (num * 3) + 1
hasil_sequence.append(num)

print(hasil_sequence)