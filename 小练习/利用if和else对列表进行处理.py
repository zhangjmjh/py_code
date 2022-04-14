

#   利用if和else的操作，可以基于某些条件过滤数据，如下图所示。


list = list(range(1,20))

print('偶数的平方：', [i ** 2 if i % 2 ==0 else i for i in list])



'''
1、for i in list()
2、if i % 2 == 0  i ** 2 
3、else i         
'''


#  偶数的平方： [1, 4, 3, 16, 5, 36, 7, 64, 9, 100, 11, 144, 13, 196, 15, 256, 17, 324, 19]