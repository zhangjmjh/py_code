






# enumerate   在同时需要index和value值的时候可以使用  利用它可以同时获得索引和值


def get_num(str,target):
    count = 0
    for i ,j in enumerate(str):
        if j == target:
            count += 1
            print(target,'出现的位置：',i)
    print(target,'出现的次数',count)


get_num('werwerwerdfasd','w')