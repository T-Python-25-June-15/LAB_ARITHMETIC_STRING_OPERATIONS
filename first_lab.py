
sentence = "My name is Shahad, I Learning Python is so fun in tuwaiq"

word = "Python"


print("Length of the sentence:", len(sentence))

print("First occurrence of the word:", sentence.find(word))
print("Number of times the word appears:", sentence.count(word))


print("Sentence in UPPERCASE:", sentence.upper())




print("Sentence in lowercase:", sentence.lower())


new_sentence = sentence.replace(word, "Java")
print("Sentence after replacement:", new_sentence)



print("Last character of the sentence:", sentence[-1])

