def print_temper() :
    """输入一组温度数据，返回最高，最低，平均和中位数温度"""
    temperatures = []
    with open('E:\Python快速入门(3)源码\源代码\QuickPython_3rd_ed_source\qpbe3e\exercise_answers\lab_05.txt') as infile :
        for row in infile:
            temperatures.append(float(row.strip()))
    print("最高温度为：%.2f" % (max(temperatures)))
    print("最低温度为：%.2f" % (min(temperatures)))
    print("平均温度为：%.2f" % (sum(temperatures)/len(temperatures)))
    temperatures.sort() #对温度自排序
    print("中位数温度为： %.2f" % (temperatures[len(temperatures)//2]))
    print("总共有%d个温度，唯一的温度有: %d个" % (len(temperatures),len(set(temperatures))))
if __name__ == '__main__' :
    print_temper()