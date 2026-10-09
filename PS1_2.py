import numpy as np

#2.1
#创建矩阵
M1 = np.random.randint(0, 51, size=(5, 10))
M2 = np.random.randint(0, 51, size=(10, 5))

#输出创建的两个矩阵
print(M1)
print(M2)

#2.2 编写矩阵乘法函数
def Matrix_multip(matrix1, matrix2):
    #获取矩阵大小
    Row_1 = len(matrix1) #矩阵1的行数
    Col_1 = len(matrix1[0]) #矩阵1的列数
    Row_2 = len(matrix2) #矩阵2的行数
    Col_2 = len(matrix2[0])
    
    #判断能否相乘
    if Col_1 == Row_2:
        #创建一个全零矩阵
        matrix0 = np.zeros((Row_1, Col_2))
        #矩阵M1乘以矩阵M2
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    matrix0[i][j] += matrix1[i][k] * matrix2[k][j]
        return matrix0
    else:
        return None 


#调用函数计算M1 * M2
M3 = Matrix_multip(M1, M2)

# 只有当 M3 不是 None（即成功相乘）时，才打印结果
if M3 is not None:
    print(M3)
else:
    print("矩阵无法相乘！")

