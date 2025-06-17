sentence = "My name is naif alghamdi I graduated from Arab Open Univercity with a computer scince dgree"


word = "naif"

print("Length of the sentence:", len(sentence))

print("Index of first occurrence of '" + word + "':", sentence.find(word))

print("Number of times " + word + " appears:", sentence.count(word))

print("Sentence in uppercase:", sentence.upper())

print("Sentence in lowercase:", sentence.lower())

new_sentence = sentence.replace(word, "cat")
print("Sentence with word replaced:", new_sentence)

print("Last character of the sentence:", sentence[-1])

