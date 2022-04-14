

#    计算子女的身高

father_height = float(input('请输入父亲的身高：'))
mother_height = float(input('请输入母亲的身高：'))

son_height = (father_height+mother_height)*0.54
print(f'预测子女的身高为：{son_height}cm')