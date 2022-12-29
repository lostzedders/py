name='传播智客'
stoke_price=19.99
stoke_code='003032'
factor=1.2
print('请输入天数')
days=input()
stoke_price1=stoke_price * 1.2 ** float(days)
print('公司：%s，股票代码:%s,当前股价%.2f,每日的增长系数为%s，经过七天的增长后的股价为%.2f'%(name, stoke_code, stoke_price, factor, stoke_price1))
