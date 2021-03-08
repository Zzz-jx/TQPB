def clean():
    punct = str.maketrans(",-;'.", "     ")
    with open("ch6/moby_01.txt") as infile, open("ch6/moby_01_clean.txt", "w") as outfile:
        for line in infile:
            # 全都转换成大写或小写
            line = line.lower()
            # 删除标点符号
            line = line.translate(punct)
            # 拆分为单词
            words = line.split()
            cleaned_words = "\n".join(words)+"\n"
            # 将单词按行写入
            outfile.write(cleaned_words)
if __name__ == "__main__":
    clean()