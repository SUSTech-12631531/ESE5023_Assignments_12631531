#5.1 编写函数Find_expression

#定义递归函数
def Find_expression(k):
    #初始数字
    Digit = "123456789"
    
    #终止条件
    def dfs(idex, output):
        if idex == 8:
            if eval(output) == k:
               print(f"{output} = {k}")
            return
    
        #递归条件
        New_Digit = Digit[idex + 1]
        dfs(idex + 1, output + "+" + New_Digit)
        dfs(idex + 1, output + "-" + New_Digit)
        dfs(idex + 1, output + New_Digit)
        
    #初始条件
    dfs(0, Digit[0])

#选取k=50进行验证
Find_expression(50)


#5.2 编写函数Count_solutions，并找到最值解及数字      
#定义递归函数
def Count_solutions(k):
    #初始数字
    Digit = "123456789"
    #计数
    Visited = 0
    
    #终止条件
    def dfs(idex, output):
        nonlocal Visited
        if idex == 8:
            if eval(output) == k:
               Visited += 1
            return
        
        #递归条件
        New_Digit = Digit[idex + 1]
        dfs(idex + 1, output + "+" + New_Digit)
        dfs(idex + 1, output + "-" + New_Digit)
        dfs(idex + 1, output + New_Digit)
    
    #初始条件
    dfs(0, Digit[0])
    #计数
    return Visited

# 统计 1 到 100解个数
Total_solutions = [Count_solutions(k) for k in range(1, 101)]

# 求最值解
Max_count = max(Total_solutions)
Min_count = min(Total_solutions)
print(Max_count)
print(Min_count)

#求最值解对应数字
for i, c in list(enumerate(Total_solutions)):
    if c == max(Total_solutions):
        print(f"最大值对应数字：{i + 1}")
    elif c == min(Total_solutions):
        print(f"最小值对应数字：{i + 1}")