name = "Miftah Furqaanul Haq"
split_name = name.split()
name_len = len(split_name)
for i  in range(name_len):
    if split_name[i][0] == split_name[0][0] or split_name[i][0] == split_name[name_len-1][0]:
        print(split_name[i][0], end = ".")

