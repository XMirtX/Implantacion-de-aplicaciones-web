import sys

string = str(sys.argv[1])


def count_words(sentence):
    summary = {}
    list_str = string.split(" ")
    for char in list_str:
        if char in summary:
            summary[char] += 1
        else:
            summary[char] = 1
    return summary
for name, number in (count_words(string).items()):
    print(name, ":", number)
