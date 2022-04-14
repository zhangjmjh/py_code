






dict1 = {'name':['james','alice'], 'num':['31209','3152015']}
dict2 = {'SEX':['N','F']}

ret = {**dict1,**dict2}
print(ret)   #  {'name': ['james', 'alice'], 'num': ['31209', '3152015'], 'SEX': ['N', 'F']}