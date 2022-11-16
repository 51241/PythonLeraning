def tm006():
    l = [0, 1]
    for i in range(10):
        arr = l[-2:]
        l.append(arr[0] + arr[1])
        print(i)
        print(arr)
    print(l)
