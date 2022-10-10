def sort_words(input):
    words = input.split()
    words.sort(key=str.lower)
    return words


while (True):
    test = input("Enter some words: ")
    print(sort_words(test))
