# 用于测试全局变量和局部变量
def fun1():
    global a
    a = 1
    print("in fun(), a = {0}, b = {1}".format(a, b))

if __name__ == "__main__":
    a = "one"
    b = "two"
    print("before fun(), a = {0}".format(a))
    fun1()
    print("after fun(), a = {0}".format(a))