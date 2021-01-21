print("------列表推导式------")
# 用推导式生成一个0-10的列表
list1 = [i for i in range(10)]
print(list1)

# 创建一个0 - 10的偶数列表
list1 = [i for i in range(0,10,2)]
print(list1)

list1 = [i for i in range(10) if i % 2 == 0]
print(list1)

# 多个for循环实现列表推导式
list1 = [(i,j) for i in range(1,3) for j in range(3)]
print(list1)

print("------字典推导式------")
# 创建一个字典:字典key是1-5,value是这个数字的2次方
dict1 = {i : i**2 for i in range(1,5)}
print(dict1)

#将2个列表合并成一个字典
list1 = ["name","age","gender"]
list2 = ["tom",20,"man"]

dict2 = {list1[i] : list2[i] for i in range(len(list1))}
print(dict2)

# 提取字典中目标数据 提取上述电脑中数量大于等于200的字典数据
counts = {"mbp":268,"hp":125,"dell":201,"lenovo":199,"Acer":99}
dict3 = {key:value for key,value in counts.items() if value >= 200}
print(dict3)

print("------集合推导式------")
# 创建一个集合,数据为下方列表的2次方
list1 = [1,1,2]
set1 = {i ** 2 for i in list1}
print(set1)
