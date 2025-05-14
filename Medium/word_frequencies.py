def word_frequencies(text):
    words = text.split()
    return {word: words.count(word) for word in set(words)}

text = input("text: ")
print(word_frequencies(text))
