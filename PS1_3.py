#定义帕斯卡三角函数
def Pascal_Triangle(k):
    #定义初始行
    Row = [1]
    
    #算出k行的列数
    for n in range(1, k + 1):
        New_Row = [1] * (n + 1)
        for i in range(1, n):
            New_Row[i] = Row[i - 1] + Row[i]
        Row = New_Row
    return Row

#调用函数显示帕斯卡三角第100 & 200行
print(Pascal_Triangle(100))
print(Pascal_Triangle(200))
