li_1 = ['first', 'second', 'th', [1, 2, 3]]
b = li_1.index('th')
li_1.insert(1, 'low1')
li_1.append(8)
li_1.extend([3, 4, 5])
del li_1[0]
new = li_1.pop(0)
li_1.remove('th')
co = li_1.count('second')
leng = len(li_1)
# li_1.clear()
print(li_1)
print(leng)
