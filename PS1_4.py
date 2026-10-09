def Least_moves(x):
    #初始金额
    RMB = x
    
    #金额数值转化为二进制形式
    Binary = bin(RMB)[2:]
    #print(Binary)
    
    #计算二进制数值的位数
    Digit_Binary = len(Binary)
    #print(len(Binary))
    
    #计算二进制数值中1的个数
    Count = Binary.count('1')
    #print(Count)
            
    #得到步数        
    Step = Digit_Binary + Count - 2
    return Step

print(Least_moves(874929))