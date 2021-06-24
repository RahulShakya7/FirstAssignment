def outer_fun():
    a = 20

    def inner_function():
        a = 30
        print('inner:', a)

    inner_function()
    print('a :', a)


a = 10
outer_fun()
print('a :', a)

def outer_fun():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('inner:', a)

    inner_function()
    print('a :', a)


a = 10
outer_fun()
print('a :', a)
