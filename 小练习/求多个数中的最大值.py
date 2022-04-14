









def get_max(*args):
    x = args[0]
    for i in args:
        if i > x:
            x = i
    return x
print(get_max(3, 8, 9, 3, 6, 3)) # 9