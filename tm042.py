def tm042():
    num = 5
    def autofunc():
        num  = 1
        print("The num is %d" %num)
        num += 1



    for i in range(3):
        print("the num is %d" % num)
        num += 1
        autofunc()


tm042()
