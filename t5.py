print('欢迎来到黑马动物园')
height = float(input('请输入您的身高(cm)'))
if height > 120:
    print('您需要补票十元')
elif height < 80:
    print('too short')
else:
    print('您可以免费游玩')
