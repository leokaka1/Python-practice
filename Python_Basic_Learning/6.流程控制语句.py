# 1. if
name = "haha"

if name == "leon":
    print(f"he name is {name}")
elif name == "sisi":
    print(f"she name is {name}")
else:
    print("he has no name")

print("------------------------------------")

# 2. while
i = 0

while i < 5:
    print("hahahah")
    i = i+1

print("------------------------------------")

# 3. for循环
str1 = "leon"
for i in str1:
    print(f"循环打印 ----- {i}")


# 4. break 和 continue
"""
• continue 用于跳过当前循环的剩余语句
• break关键字用来终止循环语句
"""

print("------------------------------------")

for i in str1:
    if i == "n":
        print("碰到了e跳出")
        break
    else:
        print(f"break打印 ----- {i}")

print("------------------------------------")

for i in str1:
    if i == "e":
        print("碰到了e跳出")
        continue
    else:
        print(f"continue打印 ----- {i}")



