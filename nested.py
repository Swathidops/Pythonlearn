def f1():
    print('Hi F1')
    def f2():
        print('Hi F2')
    print('Second F1')
    f2()
f1()

