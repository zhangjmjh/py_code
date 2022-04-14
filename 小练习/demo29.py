
# 下面是一个父类三个子类
class Instrument():
    pass

class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')

class Play(Instrument):
    def make_sound(self):
        print('钢琴在演奏')

class Violin(Instrument):  # 不管什么类  这里只要有make_sound 方法就可以使用play这个类
    def make_sound(self):
        print('小提琴在演奏')

class Bird():
    def make_sound(self):
        print('小鸟在唱歌')

def play(instrument):   #  这是演奏的函数
    instrument.make_sound()


if __name__ == '__main__':
    play(Erhu())
    play(Play())
    play(Violin())
    play(Bird())