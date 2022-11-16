import numpy as np
def tm038():
    a = np.arange(25).reshape(5,5)
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 +=a[i][i]
    for k in range(len(a)):
        sum2 +=a[k][len(a)-k-1]
    print("左对角线元素的总和为：",sum1)
    print("右边对角线元素的总和为：",sum2)
    print(a)

tm038()