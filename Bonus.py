
sentence = "Hey Twuiq Acdamy i'm Student to Python-Camp this is test lab to use python <3"

word = "Python"


print("Length of the sentence:", len(sentence))


print("First occurrence of the word:", sentence.find(word))


print("Number of occurrences of the word:", sentence.lower().count(word.lower()))


print("Uppercase:", sentence.upper())


print("Lowercase:", sentence.lower())

new_sentence = sentence.replace("Python", "a")
print("Replaced sentence:", new_sentence)


print("Last character of the sentence:", sentence[-1])
