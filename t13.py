# li = [21, 25, 21, 23, 22, 20]
# li.append(31)
# li.extend([29, 33, 30])
# out1 = li[0]
# out2 = li[-1]
# in31 = li.index(31)
# index = 0
# # while index < len(li):
# #     a = li[index]
# #     print(a)
# #     index += 1
#
# for a in li:
#     print(a)
# # print(f'{out1}, {out2}, {in31}')

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
out = []
while index < len(li):
    ele = li[index]
    n = 0
    if ele % 2 == 0:
        out.append(ele)
        n += 1
    index += 1
print(out)

# out1 = []
# for x in li:
#     n = 0
#     if x % 2 ==0:
#         out1.append(x)
#         n += 1
# print(out1)
# 元组里面嵌套 list ， list的内容可以修改
