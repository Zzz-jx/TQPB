# 动手题
def decorate(func):
    print("in decorate function, decorating", func.__name__)
    def wrapper_func(args):
        print("<html>\n\t--")
        func(args)
        print("/<html>")
    return wrapper_func

if __name__ == "__main__":
    @decorate # 类似于注解用法
    def myfunction(para):
        print(para)
    myfunction("hello")
