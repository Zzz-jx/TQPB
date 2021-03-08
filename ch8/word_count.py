""" Reads a file and return the number of lines,
 words and characters - similar to the UNIX wc utility"""
infile = open("./ch8/word_count.tst")

lines = infile.read().split("\n")

line_count = len(lines)
word_count = 0
char_count = 0

punct = str.maketrans(",.", "  ")
for line in lines:
    line = line.translate(punct)
    words = line.split() # 分割每一行为单个单词
    word_count += len(words) # 记录单词数
    char_count += len(line) # 记录字符数
    print(words)

print("File has {lc} lines, {wc} words, {cc} characters".format(
    lc = line_count, wc = word_count, cc = char_count))
