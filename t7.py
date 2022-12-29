age = int(input('请输入年龄'))
if age > 18:
    print('年龄达标了')
    if age < 30:
        print('但是还不能领取')
    else:
        print('可以领取')
else:
    print('不可以领取')