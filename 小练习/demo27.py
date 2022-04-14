

class Student(object):
    def __init__(self,stu_name,stu_age,stu_gender,stu_score):
        self.stu_name = stu_name
        self.stu_age = stu_age
        self.stu_gender = stu_gender
        self.stu_score = stu_score
    def show(self):
        print(self.stu_name,self.stu_age,self.stu_gender,self.stu_score)

if __name__ == '__main__':
    print('请输入五位学员的信息：（姓名#年龄#性别#成绩）')
    list = []
    for i in range(0,5):
        s = input(f'请输入第{i+1}个学生的信息和成绩：')
        s_list = s.split("#")
        # 创建学生对象
        stu = Student(s_list[0],int(s_list[1]),s_list[2],float(s_list[3]))
        list.append(stu)
    # 遍历列表
    for item in list:
        # item 这里面存储了学生对象，是一个对象 既然是对象就可以调用show()方法
        item.show()