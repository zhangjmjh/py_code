









list = [5, 23, 3, 2, 54, 4, 6, 8, 856]
list_len = len(list)  #9

for i in range(list_len-1):  #8
    for j in range(i, list_len):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)  # 结果：[2, 3, 4, 5, 6, 8, 23, 54, 856]

# i 取 0时 j 会取0，1，2，3，4，5，6
# i 取1时，j也会轮流取1 2 3 4 5 6




