"""
单继承
"""

class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

class B(A):
    pass

result = B()
result.info_print()

"""
多继承
"""

class A(object):
    def testA(self):
        print("this is A class")

class B(object):
    def testB(self):
        print("this is B class")

class C(A,B):
    pass

c = C()
c.testA()
c.testB()


"""
子类重写父类方法
"""
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)

class B(A):
    def info_print(self):
        print(self.num + 1)

result = B()
result.info_print()

"""
子类调用父类的同名方法和属性
"""

class A(object):
    def testA(self):
        print("this is A class")

class B(object):
    def testB(self):
        print("this is B class")

class C(A,B):

    def testA(self):
        self.__init__(self)
        print("hello world")

    def testAmathod(self):
        A.__init__(self)
        A.testA(self)

c = C()
c.testAmathod()
c.testB()

"""
super调用父类方法
"""
class A(object):
    def testA(self):
        print("this is A class")

class B(object):
    def testB(self):
        print("this is B class")

class C(A,B):

    def testA(self):
        self.__init__(self)
        print("hello world")

    def testAmathod(self):
        super().__init__()
        super().testA()

c = C()
c.testAmathod()
c.testB()

"""
私有方法
"""

class A(object):
    def __hello_world(self):
        print("nice")

    def out_print(self):
        self.__hello_world()

a = A()
a.out_print()


"""
调用或修改私有属性
一般用
get_属性 / 获取
set_属性 / 设置
"""
class B(object):
    def __init__(self):
        self.kongfu = "煎饼果子"
        self.__money = 200000

    #获取私有属性
    def get_money(self):
        return self.__money

    #修改私有属性
    def set_money(self,count):
        self.__money = count

    def out_print(self):
        self.__hello_world()


b = B()
b.set_money(1500)
money=b.get_money()
print(money)


