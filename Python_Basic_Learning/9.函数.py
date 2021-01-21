"""
1.函数的定义
def 函数名(参数):
    代码1
    代码2

2.函数的调用
函数名(参数)

注意:
1) 不同的需求,参数可有可无
2) 在Python中,函数必须<先定义后使用>
"""


# 封装ATM机功能选项
def select_func():
    print("----请选择功能------")
    print("查询余额")
    print("存款")
    print("取款")
    print("------请选择功能------")


print("密码正确登录成功")
select_func()

"""
函数参数的作用
"""


def add_num(a, b):
    result = a + b
    print(result)


add_num(1, 3)

"""
函数返回值的作用
"""


def buy():
    return "烟"


goods = buy()
print(goods)


"""
函数的嵌套调用
"""

def testB():
    print("----testB start----")
    print("这里是testB函数执行代码....")
    print("---- testB end ----")

def testA():
    print("----TestA start----")
    testB()
    print("----TestA end----")

testA()


"""
变量的作用域
变量分局部变量和全局变量
在函数内部就是局部变量,外部是不能修改的.但是如果是全局变量就能修改

但是如果全局变量也只能在函数内部修改,如果要修改全局变量,则要重新定义个global变量来重新解释一下全局变量

例如:如果定义个一个全局变量a, 要在testB方法中修改全局变量,则
"""
a = 100

def testA():
    print(a)

def testB():
    global a
    a = 200
    print(a)

testA()
testB()
print(f"全局变量a={a}")


"""
关键字参数
"""
def user_info(name,age,gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

user_info("rose",age=20,gender="女")
user_info("小名",gender="男",age=16)

"""
缺省参数
"""
user_info("Tom",20)

"""
不定长参数
"""

def user_info(*args):
    print(args)

user_info("Tim")
user_info("Tom",18)




