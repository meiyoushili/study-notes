#变量和类型
a=10
b=3.14
c="hello"
d=True
e=None
print(type(a))
print(type(b))
#类型转换
x=float(a)
y=int(b)
z=str(123)
#字符串
name="张三"
age=25
#f-string（最常用的格式化方式）
msg=f"我叫{name},今年{age}岁"
print(msg)
#字符串方法
text="Hello World"
print(text.strip())    # "Hello World"
print(text.lower())    # "  hello world  "
print(text.upper())    # "  HELLO WORLD  "
print(text.replace("World","Python"))   # "  Hello Python  "
print(text.split())     # ['Hello', 'World']
print(len(text))  # 14

#索引和切片
s="python"
print(s[0])    #第一个
print(s[-1])    #最后一个
print(s[0:3])    #前三个
print(s[::-1])   #反转

# ========== 3. 输入输出 ==========
name=input("请输入你的名字")   #Python 是动态类型语言：变量名只是一个标签，不需要提前声明类型。Python 会在运行时根据你赋的值自动判断类型
print(f"你好,{name}")     #f 的意思是 f-string（格式化字符串）。告诉 Python：这个字符串里有 {变量} 需要替换成实际值
age=int(input("请输入你的年龄"))
print(f"明年你{age+1}岁")

# ========== 4. if 语句 ==========
a = 10
b = 20

if a>b :
    print("a大")
elif a==b:
    print("一样大")
else:
    print("b大")

# 逻辑运算符：and / or / not
if a>0 and b>0 :
    print("都是正数")
if a<0 or b<0 :
    print(False)
if not a>5:
    print(False)

# ========== 5. 循环 ==========
# range
for i in range(5):
    print(i)
for i in range(2,10,2):
    print(i)
# 遍历列表
fruits=["苹果","香蕉","橘子"]
for fruit in fruits:
    print(fruit)
#while
i=0
while i<5:
    print(i)
    i=i+1        # Python没有 i++

# break / continue
for i in range(10):
    if i==3:
        continue
    if i==7:
        break
    print(i)

