def count_cleaned_words():
    count_words = {}
    most_frequently_word = ""
    least_frequently_word = ""
    with open("D:\SourceCode\PythonScript\ch6\moby_01_clean.txt") as infile:
        for line in infile:
            word = line.strip()
            count_words[word] = count_words.get(word, 0) + 1
            if most_frequently_word == "":
                most_frequently_word = word
            if least_frequently_word == "":
                least_frequently_word = word
            if count_words[most_frequently_word] < count_words[word]:
                most_frequently_word = word
            if count_words[least_frequently_word] > count_words[word]:
                least_frequently_word = word
    print("most frequent word is \"{0}\" for {2} times\n\
least frequent word is \"{1}\" for {3} times".format(most_frequently_word, least_frequently_word, count_words[most_frequently_word], count_words[least_frequently_word]))
if __name__ == "__main__":
    count_cleaned_words()
