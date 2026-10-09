
#输入三个值
int_val = input("Enter three numbers: (eg. 3,2,1) ")

#转换
a, b, c = map(float, int_val.split(','))

#显示输入的三个值
print("three numbers:", int_val)

#对前三个值进行排序
diff_1 = a - b
if diff_1 > 0:
    diff_2 = b - c
    if diff_2 > 0:
       print(a, b, c)
    else:
        diff_3 = a - c
        if diff_3 > 0:
            print(a, c, b)
        else:
            print(c, a, b)
else:
    diff_2 = b - c
    if diff_2 > 0:
        pass
    else:
        print(c, b, a)
