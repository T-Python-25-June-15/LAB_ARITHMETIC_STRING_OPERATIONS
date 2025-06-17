sentence = "My name is Hassan Abdullah And I'm interested in web development"

word = "web"

print("Length of the sentence:", len(sentence))

print("First occurrence of the word:", sentence.find(word))

print("Number of times the word appears:", sentence.count(word))

print("Uppercase: "  , sentence.upper())

print("Lowercase: ", sentence.lower())

new_sentence = sentence.replace(word, "Django")
print("Replaced sentence:", new_sentence)

print("Last character of the sentence:", sentence[-1])
