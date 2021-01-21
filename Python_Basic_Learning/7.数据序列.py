print("---------- 字符串 ----------")
def string():
    """
    去空格或者特殊符号
    """
    from filecmp import cmp

    s = " hello , world !"
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    """
    连接字符串
    """
    sStr1 = "strcat"
    sStr2 = "append"
    sStr1 += sStr2
    print(sStr1)

    """
    查找字符串
    """
    sStr1 = "strchr"
    sStr2 = "r"
    nPos = sStr1.index(sStr2)
    print(nPos)

    """
    字符串比较
    """
    sStr1 = "strchr"
    sStr2 = "strch"

print("---------- 列表 ----------")
def list():
    name_list = ['Tom', 'Lily', 'Rose']
    print(name_list[0])  # Tom
    print(name_list[1])  # Lily
    print(name_list[2])  # Rose

    # index()：返回指定数据所在位置的下标
    # 列表序列.index(数据, 开始位置下标, 结束位置下标)
    print(name_list.index("Tom", 0, 2))

    # count()：统计指定数据在当前列表中出现的次数。
    name_list = ['Tom', 'Lily', 'Rose']
    print(name_list.count('Lily'))  # 1

    # len()：访问列表⻓度，即列表中数据的个数。
    name_list = ['Tom', 'Lily', 'Rose']
    print(len(name_list))  # 3

    # 判断是否存在
    # in：判断指定数据在某个列表序列，如果在返回True，否则返回False

    name_list = ['Tom', 'Lily', 'Rose']
    # 结果：True
    print('Lily' in name_list)
    # 结果：False
    print('Lilys' in name_list)

    # not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False
    name_list = ['Tom', 'Lily', 'Rose']
    # 结果：False
    print('Lily' not in name_list)
    # 结果：True
    print('Lilys' not in name_list)

    """
    增加
    """
    name_list = ['Tom', 'Lily', 'Rose']
    name_list.append('xiaoming')
    # 结果：['Tom', 'Lily', 'Rose', 'xiaoming']
    print(name_list)

    # extend()：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表。
    name_list = ['Tom', 'Lily', 'Rose']
    name_list.extend('xiaoming')
    # 结果：['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
    print(name_list)

    # insert()：指定位置新增数据。
    name_list = ['Tom', 'Lily', 'Rose']
    name_list.insert(1, 'xiaoming')
    # 结果：['Tom', 'xiaoming', 'Lily', 'Rose']
    print(name_list)

    """
    删除
    """
    name_list = ['Tom', 'Lily', 'Rose']
    # 结果：报错提示：name 'name_list' is not defined
    del name_list
    print(name_list)

    # 删除指定数据
    name_list = ['Tom', 'Lily', 'Rose']
    del name_list[0]
    # 结果：['Lily', 'Rose']
    print(name_list)

    # pop()：删除指定下标的数据(默认为最后⼀个)，并返回该数据。
    name_list = ['Tom', 'Lily', 'Rose']
    del_name = name_list.pop(1)
    # 结果：Lily
    print(del_name)
    # 结果：['Tom', 'Rose']
    print(name_list)

    # remove()：移除列表中某个数据的第⼀个匹配项。
    name_list = ['Tom', 'Lily', 'Rose']
    name_list.remove('Rose')
    # 结果：['Tom', 'Lily']
    print(name_list)

    # clear()：清空列表
    name_list = ['Tom', 'Lily', 'Rose']
    name_list.clear()
    print(name_list)  # 结果： []

    """
    修改
    """

    name_list = ['Tom', 'Lily', 'Rose']
    name_list[0] = 'aaa'
    # 结果：['aaa', 'Lily', 'Rose']
    print(name_list)

    # 逆置：reverse()
    num_list = [1, 5, 2, 3, 6, 8]
    num_list.reverse()
    # 结果：[8, 6, 3, 2, 5, 1]
    print(num_list)

    """
    排序：sort()
    """

    num_list = [1, 5, 2, 3, 6, 8]
    num_list.sort()
    # 结果：[1, 2, 3, 5, 6, 8]
    print(num_list)

    """
    复制
    """
    name_list = ['Tom', 'Lily', 'Rose']
    name_li2 = name_list.copy()
    # 结果：['Tom', 'Lily', 'Rose']
    print(name_li2)

print("---------- 字典 ----------")
def dict():
    """
    创建字典
    """
    dict1 = {"name": "tom", "age": 20, "gender": "man"}
    # 空字典
    dict2 = {}
    dict3 = ()

    print("----------字典的常见操作----------")

    print("-----增-----")
    """
    注意: 如果key存在则修改这个key对应的值,如果key不存在则新增此键值对
    """
    dict1 = {"name": "Tom", "age": 20, "gender": "男"}
    dict1["name"] = "lili"
    print(dict1)

    dict1["id"] = 110
    print(dict1)

    print("-----删-----")
    """
    del()/del : 删除字典或者删除字典中指定的键值对
    """
    del dict1["gender"]
    print(dict1)

    """
    clear(): 清空字典
    """
    dict1.clear()

    print("-----改-----")
    dict1 = {"name": "Tom", "age": 20, "gender": "男"}
    dict1["name"] = "james"

    print("-----查-----")
    print(dict1["name"])
    # print(dict1["id"]) 报错,因为没有对应的值

    """
    get() 
    字典.get(key,默认值)
    如果当前查找的key不存在则返回第二个参数(默认值),如果省略第二个参数,则返回none
    """
    print(dict1.get("name"))
    print(dict1.get("id", 110))  # 110
    print(dict1.get("id"))  # none

    """
    keys() 
    返回所有的key
    """
    print(dict1.keys())

    """
    values() 
    返回所有的values
    """
    print(dict1.values())

    """
    values() 
    返回所有的items
    """
    print(dict1.items())

    print("----------字典的循环遍历----------")

    print("---遍历字典的key---")
    for key in dict1.keys():
        print(key)

    print("---遍历字典的values---")
    for value in dict1.values():
        print(value)

    print("---遍历字典的items---")
    for items in dict1.items():
        print(items)

    print("---遍历字典的键值对---")
    for key, value in dict1.items():
        print(f"{key} = {value}")

    print("---迭代器迭代index和key值---")
    for index,key in enumerate(dict1):
        print(f"{index} = {key}")

print("---------- 元组 ----------")
def tuple():
    """
    元祖的应用场景

    思考:如果想要存储多个数据,但是这些数据是不能修改的数据,怎么做?
    一个元祖可以存储多个数据,元祖中的数据是不能修改的
    """

    print("----------定义元祖----------")
    """
    定义元祖
    多个数据元祖
    t1 = (10,20,30)

    单个元祖
    t2 = (10,)
    如果定义的元祖只有一个数据,那么这个数据后面也要添加都好,否则数据类型为唯一的这个数据的数据类型,例如
    """

    t2 = (10,)
    print(type(t2))

    t3 = (20)
    print(type(t3))

    t4 = ("hello")
    print(type(t4))

    print("----------元祖的常见操作----------")

    """
    按下标查找数据
    """
    tuple1 = ("aa", "bb", "cc", "dd")
    print(tuple1[0])

    """
    查找数据下标
    """
    print(tuple1.index('aa'))

    """
    统计某个数据在当前元祖中出现的次数
    """
    print(tuple1.count("bb"))

    """
    统计元祖中数据个数
    """
    print(len(tuple1))

print("---------- 集合 ----------")
def set():
    """
    创建集合
    创建集合使用{}或者set(),但是如果创建空集合只能用set(),因为{}是用来创建空字典的
    """
    s1 = {10, 20, 30, 40, 50}
    s2 = {10, 10, 20, 20, 30, 30}
    s3 = set("abcdefg")
    s4 = set()

    print("------集合的常见操作方法------")
    print("---增加数据---")
    """
    add
    因为集合有去重功能,所以,当向集合内追加的数据是当前集合已有数据的话,则不进行任何操作
    """
    s1 = {10, 20}
    s1.add(100)
    s1.add(20)
    print(s1)

    """
    update()
    追加的数据是序列
    """
    s1.update([100, 200])
    s1.update("abc")
    print(s1)

    print("---删除数据---")
    """
    remove()
    删除集合中的指定数据,如果数据不存在则报错
    """
    s1.remove(10)
    print(s1)

    """
    discard()
    删除集合中的指定数据,如果数据不存在则报错
    """
    s1.discard(20)

    """
    pop()
    随机删除集合中的某个数据,并返回这个数据
    """
    s2 = {10, 20, 30, 40, 50, 60}
    s2.pop()
    print(s2)

    print("---查找数据---")
    """
    in:判断数据在集合中的序列
    not in: 判断数据不在集合序列
    """
    print(10 in s2)
    print(10 not in s2)


if __name__ == '__main__':
     dict()