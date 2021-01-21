"""
定义类
class 类名():
    代码
    ....
"""

class Washer():
    def wash(selfs):
        print("我会洗衣服")

"""
创建对象
对象名 = 类名()
"""

#创建对象
haier1 = Washer()
print(haier1)

haier1.wash()

"""
类外面添加对象属性
对象名.属性名 = 值
"""

haier1.width =500
haier1.height = 800

"""
类外面获取对象的属性
对象名.属性名
"""
print(f"haier1洗衣机的宽度是{haier1.width}")
print(f"haier1洗衣机的高度是{haier1.height}")

"""
类里面获取对象的属性
self.属性名
"""

class Washer():
    def print_info(self):
        print(f"haier1洗衣机的宽度是{self.width}")
        print(f"haier1洗衣机的高度是{self.height}")

haier2 = Washer()

haier2.width = 500
haier2.height = 800

haier2.print_info()

"""
魔法方法
"""

class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800

    def print_info(self):
        print(f"洗衣机的宽度是{self.width},高度是{self.height}")

haier3 = Washer()
haier3.print_info()


"""
带参数的init
"""
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f"洗衣机的宽度是{self.width},高度是{self.height}")

haier4 = Washer(10,20)
haier4.print_info()


"""
__str__()
当使用print输出对象的时候,默认打印对象的内存地址,如果类定义了__str__方法,那么就会打印从这个方法中return的数据
"""
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return "这是洗衣机的说明书"

    def print_info(self):
        print(f"洗衣机的宽度是{self.width},高度是{self.height}")

haier5 = Washer(10,20)
haier5.print_info()
print(haier5)

"""
__del__()
当删除对象时候,python解释器也会默认调用__del()方法
"""
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return "这是洗衣机的说明书"

    def __del__(self):
        print(f"对象已经被删除")

    def print_info(self):
        print(f"洗衣机的宽度是{self.width},高度是{self.height}")

haier6 = Washer(10,20)
haier6.print_info()
del haier6
