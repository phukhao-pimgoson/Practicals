def main():
    word_count = {}
    string = (input("Enter your text string here: ")).split()
    if len(string) == 0:
        string.append("VOID")
    for word in string:
        frequency = word_count.get(word, 0)
        word_count[word] = frequency + 1
    string = list(word_count.keys())
    string.sort()
    for word in string:
        print("{:{}}: {}".format(word, max((len(word) for word in string)), word_count[word]))


main()
