name = input('请输入您的姓名')
money = 10000

def cx():
    global money
    print('--------查询余额--------')
    print(f'{name}，您好，您的余额为{money}元')

def ck(x):
    global money
    money += x
    print('--------存款--------')
    print(f'{name},您好，您存款{x}元成功，账户余额{money}元')

def qk(x):
    global money
    money -= x
    print('--------取款--------')
    print(f'{name},您好，您取款{x}元成功，账户余额{money}元')

def main():
    print('--------主菜单--------')
    print(f'{name},您好，欢迎来到银行，请选择操作')
    print('查询余额 【输入1】')
    print('存款    【输入2】')
    print('取款    【输入3】')
    print('退出    【输入4】')
    return int(input('选择您的操作'))

while True:
    key_in = main()
    if key_in == 1:
        cx()
        continue
    elif key_in == 2:
        num = int(input('请输入存款金额'))
        ck(num)
        continue
    elif key_in == 3:
        num = int(input('请输入取款金额'))
        qk(num)
        continue
    else:
        break


