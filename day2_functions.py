"""
第2天：函数与数据结构
包含：重复代码改写、列表统计（处理空列表）、字典字段提取（处理缺失）、5道小练习。
"""

# ============================================================
# 任务 1：把重复代码改写成函数；练习参数、返回值、默认参数
# ============================================================

def greet(name, greeting="你好"):
    """
    演示默认参数。
    如果调用时只传 name，greeting 默认为 "你好"。
    """
    return f"{greeting}，{name}！"

# 测试任务 1
print("--- 任务 1：函数基础 ---")
print(greet("小明"))                # 使用默认参数
print(greet("Alice", "Hello"))      # 覆盖默认参数


# ============================================================
# 任务 2：统计列表的最大值、最小值、平均值；处理空列表
# ============================================================

def analyze_listm(numbers):
    if not numbers:
        return None,None,None
    maxx=max(numbers)
    minn=min(numbers)
    avgg=sum(numbers)/len(numbers)
    return maxx,minn,avgg

print("liebiao[10,90,100]的最大值，最小值，平均值分别是：",analyze_listm([10,90,100]))

def analyze_list(numbers):
    """
    计算列表的 max, min, avg。
    边界情况：如果传入空列表，无法计算，返回 None 组成的元组。
    """
    # 边界处理：空列表
    if not numbers: 
        return None, None, None
    
    max_val = max(numbers)
    min_val = min(numbers)
    avg_val = sum(numbers) / len(numbers)
    
    return max_val, min_val, avg_val

# 测试任务 2
print("\n--- 任务 2：列表统计 ---")
print("正常列表 [10, 20, 30]:", analyze_list([10, 20, 30]))
print("空列表 []:", analyze_list([])) # 验证边界情况


# ============================================================
# 任务 3：从字典列表中提取指定字段；缺少字段时给出默认值
# ============================================================

def extract_dl(data_list,target_fields,default_value="N/A"):
    result=[]
    for item in data_list:
        extracted_item={}
        for field in target_fields:
            extracted_item[field]=item.get(field,default_value)
        result.append(extracted_item)
    return result
print("\n--- 任务 3：字典字段提取 ---")
users = [
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30},  # 缺少 city 字段
    {"name": "王五"}             # 缺少 age 和 city 字段
]
resulty=extract_dl(users,["name","age"],default_value="未知")
print(resulty)
def extract_fields(data_list, target_fields, default_value="N/A"):
    """
    从字典列表中提取指定字段。
    参数：
        data_list: 包含多个字典的列表
        target_fields: 需要提取的字段名列表，如 ["name", "age"]
        default_value: 如果字典中缺少该字段，使用的默认值
    返回：
        包含提取结果的新字典列表
    """
    result = []
    for item in data_list:
        extracted_item = {}
        for field in target_fields:
            # 使用 .get() 方法，如果键不存在，返回 default_value
            extracted_item[field] = item.get(field, default_value)
        result.append(extracted_item)
    return result

# 测试任务 3
print("\n--- 任务 3：字典字段提取 ---")
users = [
    {"name": "张三", "age": 25, "city": "北京"},
    {"name": "李四", "age": 30},  # 缺少 city 字段
    {"name": "王五"}             # 缺少 age 和 city 字段
]
# 提取 name 和 city 字段
extracted_users = extract_fields(users, ["name", "city"], default_value="未知")
print(extracted_users)


# ============================================================
# 任务 4：5 道小练习及边界情况解释
# ============================================================
print("\n--- 任务 4：5 道小练习 ---")

# 练习 1：计算数字列表的平方
# 输入: [1, 2, 3] -> 输出: [1, 4, 9]
# 边界: 空列表 [] -> 输出: []

def square_list(nums):
    return [n ** 2 for n in nums]

# 练习 2：统计字符串中每个字符出现的次数
# 输入: "hello" -> 输出: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# 边界: 空字符串 "" -> 输出: {}
def counter(string):
    result={}
    if not string:
        return "{}"
    for c in string:
        result[c]=result.get(c,0)+1
    return result
print("练习2 (字符统计):", counter("hello"), "| 边界(空):", counter(""))
def count_chars(text):
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

# 练习 3：反转列表（不使用内置 reverse() 方法）
# 输入: [1, 2, 3] -> 输出: [3, 2, 1]
# 边界: 单元素列表 [1] -> 输出: [1]
def reverse_list(lst):
    return lst[::-1]  # 使用切片

# 练习 4：判断一个数是否为偶数
# 输入: 4 -> 输出: True; 输入: 7 -> 输出: False
# 边界: 0 -> 输出: True (0是偶数); 负数 -2 -> 输出: True
def is_even(num):
    return num % 2 == 0

# 练习 5：合并两个字典（如果键冲突，第二个字典覆盖第一个）
# 输入: d1={'a':1}, d2={'b':2, 'a':3} -> 输出: {'a': 3, 'b': 2}
# 边界: 两个空字典 {} 和 {} -> 输出: {}
def merge_dicts(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result

# 运行并打印 5 道练习的结果
print("练习1 (平方):", square_list([1, 2, 3]), "| 边界(空):", square_list([]))
print("练习2 (字符统计):", count_chars("hello"), "| 边界(空):", count_chars(""))
print("练习3 (反转):", reverse_list([1, 2, 3]), "| 边界(单元素):", reverse_list([1]))
print("练习4 (偶数判断):", is_even(4), is_even(7), "| 边界(0):", is_even(0))
print("练习5 (合并字典):", merge_dicts({'a': 1}, {'b': 2, 'a': 3}), "| 边界(空):", merge_dicts({}, {}))