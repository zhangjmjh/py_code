





def CheckStr(gen1, gen2):
    return sorted(gen1) == sorted(gen2)

print(CheckStr('python','python'))   # True
print(CheckStr([1,21,2], [3,2,1]))   # False
