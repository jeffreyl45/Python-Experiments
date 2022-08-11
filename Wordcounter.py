def countWords(theSentence):
    words = 0
    wordStart = False
    for char in theSentence:
        if wordStart and not char.isalpha():
            words = words + 1
            wordStart = False
        elif char.isalpha():
            wordStart = True
    if wordStart:
        words = words + 1
    return words


sentence = input("What is your sentence? ")

wordcount = countWords(sentence)
print("There are %i words in your sentence" % wordcount)





