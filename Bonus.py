# Define a string variable containing a sentence with at least 10 words.
sentence:str = "Lama Alfreah"

# Define a string variable containing a word that appears in the sentence.
word:str = "Alfreah"

# Print the length of the sentence.
print("Length of sentence:", len(sentence))

# Print the index of the first occurrence of the word in the sentence.
print("Index for the first occurrence of word:", sentence.find(word))

# Print the number of times the word appears in the sentence.
print("Number of times word appears:", sentence.count(word))

# Print the sentence in all uppercase letters.
print("Uppercase:", sentence.upper())

# Print the sentence in all lowercase letters.
print("Lowercase:", sentence.lower())

# Replace the word in the sentence with a new word of your choice.
sentence = sentence.replace(word, "Abdulaziz")
print("Replaced sentence:", sentence)

# Print the last character of the sentence.
print("Last character:", sentence[-1])
