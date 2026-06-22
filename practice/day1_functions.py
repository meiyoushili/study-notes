# ========== 函数（对比 C++）==========
# C++: int add(int a, int b) { return a + b; }
# Python：
def add(a,b):
    return a+b
result=add(3,5)
print(result)

# === 默认参数 ===
def greet(name, greeting="你好"):   # greeting 有默认值，不传就用"你好"
    return f"{greeting}，{name}"

print(greet("张三"))                # 你好，张三
print(greet("李四", "Hello"))       # Hello，李四

# === 多个返回值 ===
# C++ 要返回多个值得用结构体或 tuple
# Python 直接用逗号就行
def min_max(nums):
    return min(nums), max(nums)     # 自动打包成元组返回

low, high = min_max([3, 1, 4, 1, 5])
print(low, high)                    # 1 5

# === if __name__ 用法 ===
# 作用：这个文件被直接运行时才执行下面的代码
#      被别的文件 import 时不执行
def test():
    print("函数测试")

if __name__ == "__main__":
    # 这下面的代码只有直接运行这个文件时才会执行
    test()
    print("直接运行时打印这行")

def is_palindrome(s):
    """判断字符串是否为回文，返回 True/False"""
    return s == s[::-1]

# 测试
print(is_palindrome("abcba"))   # True
print(is_palindrome("hello"))   # False

# 带输入版本（在函数外面做）
text = input("请输入一个字符串：")
if is_palindrome(text):
    print(f"{text} 是回文")
else:
    print(f"{text} 不是回文")

from collections import defaultdict,Counter
def word_frequency(text):
    words=text.split()
    counter=Counter(words)
    return counter.most_common(3)

text1=input("请输入一段文本")
print(word_frequency(text1))