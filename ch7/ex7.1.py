# 输入3个用户名和年龄，再输入一个用户名，返回相应的年龄
name_age_dict = {}
name1 = input("name 1:")
age1 = int(input("age 1:"))
name_age_dict[name1] = age1
name2 = input("name 2:")
age2 = int(input("age 2:"))
name_age_dict[name2] = age2
name3 = input("name 3:")
age3 = int(input("age 3:"))
name_age_dict[name3] = age3
required_name = input("name to print:")
print("the age of {name} is {age}".format(name = required_name, age = name_age_dict[required_name]))
