def tm010():
    import time
    a = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    time.sleep(1)
    print(a)
    b = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print(b)
    c = time.localtime(time.time())
    d = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print(c)
    print(d)

    f = time
tm010()