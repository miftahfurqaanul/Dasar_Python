# num = input("insert integer= ")
# nums = int(num)
# if nums > 0:
#     if nums%2 == 0:
#         print("this is an even number")
#     else:
#         print("this is an odd number")
# else:
#     print("tidak boleh negatif")

#ll
user_input = input("Masukkan sesuatu: ")

# Memeriksa apakah input terdiri dari hanya angka
if user_input.isdigit():
    print("Input dapat diproses")
    
    user_input = int(user_input)
    if user_input > 0:
            if user_input % 2 == 0:
                print("this is an even number")
            else:
                print("this is an odd number")
    else:
        print("tidak boleh negatif")
else:
    print("Maaf tidak bisa diproses")
