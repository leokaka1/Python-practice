"""
类属性和实例属性
类属性的有点:
- 记录的某项数据,始终保持一致时,则定义类属性
- 实例属性 要求 每个对象 为其 单独开辟一份内存空间来记录数据, 而 类属性 为全 类所共有,仅占一分内存,更加节省空间
"""

class Dog(object):
    tooth = 10

wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)
print(wangcai.tooth)
print(xiaohei.tooth)

"""
修改类属性
"""
Dog.tooth = 12
print(xiaohei.tooth)
print(wangcai.tooth)


"""
类方法
需要用装饰器@classmethod来表示为类方法,对于类方法,第一个参数必须为类对象
一般以cls作为第一个参数

类方法中需要使用类对象时(如访问私有属性时),定义类方法,
类方法一般配合类属性使用
"""

class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

wangcai = Dog()
reslut = wangcai.get_tooth()
print(reslut)


"""
静态方法
- 需要通过装饰器器 @staticmethod 来进行行行修饰,静态方方法既不不需要传递类对象也不不需要传递实例例对象
(形参没有self/cls)。
- 静态方方法 也能够通过 实例例对象 和 类对象 去访问。

静态方法使用场景
- 当方方法中 既不不需要使用用实例例对象(如实例例对象,实例例属性),也不不需要使用用类对象 (如类属性、类方方
法、创建实例例等)时,定义静态方方法
- 取消不不需要的参数传递,有利利于 减少不不必要的内存占用用和性能消耗
"""

class Dog(object):
    @staticmethod
    def info_print():
        print("这是一个狗类,用于创建狗实例")

wangcai = Dog()
reslut = wangcai.info_print()



