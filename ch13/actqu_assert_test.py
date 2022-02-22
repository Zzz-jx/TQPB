"""test assert statement"""
num = int(input("please input a integer: \n"))
try:
    assert num != 0, "you input number zero"
except AssertionError as aserror:
    print(aserror)
else:
    print("you input {0}".format(num))
