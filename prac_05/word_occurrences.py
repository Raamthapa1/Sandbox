text = input("Text: ")
words = text.split()
words.sort()
word_to_frequency = {}
for word in words:
    # checking if words is a key or not
    if word in word_to_frequency:
        word_to_frequency[word] += 1
    else:
        word_to_frequency[word] = 1
# max length of words - List comprehension
max_length = max((len(word) for word in words))
for word in word_to_frequency:
    print(f"{word:{max_length}} {word_to_frequency[word]}")
