import sys


def num_vowels(phrase):
    vowel = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in phrase.lower():
        if i in vowel:
            vowel += 1
    return  vowel


def num_whitespaces(phrase):
    whitec = 0
    for i in phrase:
        if i in " ":
            whitec += 1
    return whitec


def num_digits(phrase):
    ndigits = 0
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in phrase:
        if i in digits:
            ndigits += 1
    return  ndigits


def num_words(phrase):
    words = phrase.split(" ")
    nwords = len(words)
    return words


def reverse(phrase):
    rev = phrase[-1::-1]
    return rev


def length(phrase):
    howlong = len(phrase)
    return howlong


def halfs(phrase):
    halfs = len(phrase)
    first = phrase[halfs:]
    second = phrase[:halfs]
    return first, second


def upper_vowels(phrase):
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    for i in phrase:
        result += i.upper()
    else:
        result += i
    return result


def sorted_by_words(phrase):
    sortw = phrase.split()
    sortw.sort()
    sortedtext = "".join(sortw)
    return sortedtext


def length_of_words(phrase):
    words = phrase.split()
    wordslist = list()
    for i in words:
        size = len(i)
        wordslist.append(str(size))
    result = "".join(wordslist)
    return result

phrase = sys.argv[1]
print("Number of vowels: ", num_vowels(phrase))
print("Number of whitespaces: ", num_whitespaces(phrase))
print("Number of digits: ", num_digits(phrase))
print("Number of words: ", num_words(phrase))
print("Reverse of text: ", reverse(phrase))
print("Length of text: ", length(phrase))
print("Halfs of text: ", halfs(phrase))
print("Text with uppercased vowels: ", upper_vowels(phrase))
print("Sorted by words: ", sorted_by_words(phrase))
print("Length of words: ", length_of_words(phrase))