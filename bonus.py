# Bonus, create a new python file and do the following:
# Define a string variable containing a sentence with at least 10 words.
# Define a string variable containing a word that appears in the sentence.
# Print the length of the sentence.
# Print the index of the first occurrence of the word in the sentence.
# Print the number of times the word appears in the sentence.
# Print the sentence in all uppercase letters.
# Print the sentence in all lowercase letters.
# Replace the word in the sentence with a new word of your choice.
# Print the last character of the sentence.

TextSentence = "Hello world, My name is Nawaf Al-malki and I love so many things, for example studying programming and 3d printing, this is kind of fun actually I never regret it, so yeah there is many other things, and many other stuff"

print(f"\n\n{TextSentence}\n")

Word = "many"

print(f"The length of the sentence is: {len(TextSentence)}\n")
print(f"First occurrence of the word: {TextSentence.find(Word)}\n")
print(f"How many times the word appear: {TextSentence.count(Word)}\n")
print(f"UPPERCASE: {TextSentence.upper()}\n")
print(f"lowercase: {TextSentence.lower()}\n")

NewSentence = TextSentence.replace(Word, "Bootcamp")

print(f"Replace the word many with the word Bootcamp: {NewSentence}\n")
print(f"last character of the sentence: {NewSentence[-1]}\n")