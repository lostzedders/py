age = int(input('请输入您的年龄'))
price = 10
if age > 18:
    print('请补票%s元' % price)
    if age < 70:
        print('ok')
else:
    print('小朋友，欢迎您')
