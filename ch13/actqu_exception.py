"""using customized exception ValueTooLarge"""
class ValueTooLarge(Exception):
    pass

num = int(input("please input a integer:\n"))
try:
    if num > 1000:
        raise ValueTooLarge("you input a number that large than 1000")
except ValueTooLarge as vtl:
    print(vtl)
