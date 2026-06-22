# 列表 = C++的数组/vector，但可以装不同类型
# 创建
nums=[1,2,3,4,5]
print(nums)

# === 增加 ===
nums.append(6)  # 末尾加6
nums.insert(0,0)  #位置0插入元素0
print(nums)

# === 删除 ===
nums.pop() #删除末尾
nums.pop(0) #删除指定位置
nums.remove(3)  #删除指定元素
print(nums)

# === 查 ===
nums.index(4)  # 4在哪个位置
4 in nums   # True/False 判断有没有
print(4 in nums)
len(nums)    # 长度
print(len(nums))

# === 排序/反转 ===
nums.sort()    #小到大
print(nums)
nums.sort(reverse=True)  #大到小
print(nums)
nums.reverse() #反转
print(nums)

# === 切片（最有用的特性）===
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])        # [1,2,3] 取位置1到3
print(nums[:3])         # [0,1,2] 从头到位置2
print(nums[3:])         # [3,4,5] 从位置3到尾
print(nums[-1])         # 5 最后一个
print(nums[::-1])       # [5,4,3,2,1,0] 反转

# === 遍历 ===
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):  # 同时拿索引和值
    print(i, fruit)

# 字典 = C++的map，键值对

student = {"name": "张三", "age": 20, "score": 85.5}
# 取
print(student["name"])          # 张三（key不存在报错）
print(student.get("name"))      # 张三（推荐，不存在返回None）
print(student.get("gender", "未知"))  # 默认值

# 增/改
student["gender"] = "男"     # 新增
student["age"] = 21          # 修改

# 删
del student["score"]
student.pop("score",0)  # 删并返回，不存在返回0

#遍历
for key,value in student.items():
    print(key,value)

# 高级：defaultdict（不存在的key自动给默认值）
from collections import defaultdict,Counter

word_count=defaultdict(int)
words=["apple","banana","apple"]
for w in words:
    word_count[w] +=1
print(dict(word_count))       # {'apple':2, 'banana':1}

## Counter（专门计数）
counter = Counter(words)
print(counter.most_common(1))       # 最多： [('apple', 2)]

#text = "python java python c++ python java javascript go rust python"
# 用split拆分，统计每个词次数，输出最多的3个
text = "python java python c++ python java javascript go rust python"
print(text.split())

from collections import defaultdict,Counter
word_count=defaultdict(int)
words=text.split()
for w in words:
    word_count[w] +=1
print(dict(word_count))

counter=Counter(words)
print(counter.most_common(3))

# 创一个字典 {"张三":85, "李四":92, "王五":78}
# 算平均分、找最高分、加一个新学生、删一个
sum1=0
student={"张三":85,"李四":92,"王五":78}
for key,value in student.items():
        sum1 +=value
average=sum1/len(student)
print(average)
max1=0
for key,value in student.items():
    max1=max(value)
print(max1)