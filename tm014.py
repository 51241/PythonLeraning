def tm014():
    '''
    【个人备注】：拆到拆不动为止，类似012题。
    '''
    import math
    num = int(input('输入一个整数:'))
    arr = []
    while num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):  # 因为题目是一个没写范围正整数，开方可以有效减少该值过大时候的计算量
            if num % i == 0:
                arr.append(i)
                num = num // i
                break
        else:
            arr.append(num)
            break
    print(arr)

tm014()