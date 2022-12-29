num = int(input('请输入一个数字'))
guess_num = 10
if num == guess_num:
    print('congratus！')
elif int(input('不对，再猜一次')) == guess_num:
    print('恭喜你猜对了')
elif int(input('再猜最后一次')) == guess_num:
    print('终于猜对了')
else:
    print('真抱歉')

