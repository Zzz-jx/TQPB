def file_clean(file_name, out_name):
    punc = str.maketrans(",.:'-;", "      ")
    with open(file_name) as infile, open(out_name, "w") as outfile:
        for line in infile:
            line = line.lower() # 转换为小写
            line = line.translate(punc) # 去除标点
            words = line.split() # 拆分为单个单词
            cleaned_words = "\n".join(words) + "\n" # 把单词按每个一行排列
            outfile.write(cleaned_words)
    print("file clean finish, the cleaned file is", outfile.name)

def word_count(file_name):
    dic = {} 
    mw = "" # most frequent word 出现数量最多的单词
    lw = "" # least frquent word 出现数量最少的单词
    with open(file_name) as infile:
        for line in infile:
            word = line.strip() # 去除前后所有空白符
            dic[word] = dic.get(word, 0) + 1
            if not mw:
                mw = word
            if not lw:
                lw = word
            if dic[mw] < dic[word]:
                mw = word
            if dic[lw] > dic[word]:
                lw = word
    print("the most frequent word is \"{most}\" for {mtime} times\nthe least frequent word is \"{least}\" \
for {ltime} times".format(most = mw, least = lw, mtime = dic[mw], ltime = dic[lw]))


if __name__ == "__main__":
    # file_clean("./ch6/moby_01.txt", "./ch9/moby_01_cleaned")
    word_count("./ch9/moby_01_cleaned")