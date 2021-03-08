"""wo module. Contains function: words_occur()"""
# 接口函数
def words_occur():
    """words_occur() - count the occurences of words in a file."""
    # 提示用户输入文件名称
    file_name = input("Enter the name of the file: ")
    # 打开文件，读取单词并保存在列表中
    f = open(file_name, 'r')
    word_list = f.read().split()
    f.close()
    # 对文件中的每个单词出现的次数进行计数
    occur_dict = {}
    for word in word_list:
        # 对该单词次数加1
        occur_dict[word] = occur_dict.get(word, 0) + 1
    # 打印结果
    print("File %s has %d words (%d are unique)" \
            % (file_name, len(word_list), len(occur_dict)))
    print(occur_dict)
if __name__ == '__main__':
    words_occur()
