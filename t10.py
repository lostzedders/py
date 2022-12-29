# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j} * {i} = {j * i}\t' ,end=' ')
#     print()


# summ = 0
# for i in range(1, 10):
#     if i == 5 or i == 7:
#         continue
#     summ += i
#     print(f'i = {i}, sum = {summ}')

# 发工资
# import random
# total = 10000
# for i in range(1, 21):
#     num = random.randint(1, 10)
#     if num < 5:
#         print(f'第{i}位员工，绩效分为{num}，不发工资')
#         continue
#     elif num >= 5:
#         total -= 1000
#         print(f'第{i}位员工，绩效分为{num}，发1000，账户余额{total}')
#         if total == 0:
#             print(f'今年的工资发完了')
#             break

# 不用len函数来统计字符串长度
# 1 用 for 遍历
# str1 = 'python'
# count = 0
# for i in str1:
#     count += 1
# print(count, len(str1))
# 定义 my_len函数
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f'字符串{data}的长度为{count}')
# str1 = 'python'
# str2 = 'you'
# str3 = 'studyyyyyyyyy'
# my_len(str1)
# my_len(str2)
# my_len(str3)

# def 函数名 （传入函数:）
# 函数体
# return 返回值
# def my_sum(x, y, z):
#     return x + y + z
#
#
# print(my_sum(1, 1, 2))

# def tem(wd):
#     """
#     代码注释
#     :param wd:输入的参数
#     :return: 相加的值
#     """
#     if wd <= 37.5:
#         print(f'您的体温为{wd}°，欢迎光临')
#     else:
#         print(f'您的体温为{wd}，需要隔离')
#
#
# tem(300)

# 用 global 变量名来将函数内的变量变成全局变量，可修改
