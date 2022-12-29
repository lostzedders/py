i=1
while i <= 9:
    j=1
    while j <= i:
        res = i * j
        print('%s * %s = %s\t'% (j, i, res), end=' ')
        j +=1
    i +=1
    print()
