# Bonus, create a new python file and do the following:


#Define a string variable containing a sentence with at least 10 words.
sentence = 'I like tea, and I want to be an NLP Engineer'

#Define a string variable containing a word that appears in the sentence.
word = 'tea'

#Print the length of the sentence.
print(f'The leangth of sentense is: {len(sentence)} charecter')

# Print the index of the first occurrence of the word in the sentence.
for i in range(len(sentence)):
    if sentence[i:i+len(word)] == word:
        print(f'index of the first occurrence: {i}')

# Print the number of times the word appears in the sentence.
print(f'time appears of {word} in this {sentence}: {sentence.count(word)}')


# Print the sentence in all uppercase letters.
print(f'sentence with all uppercase letters: {sentence.upper()}')

# Print the sentence in all lowercase letters.
print(f'sentence with all lowercase letters: {sentence.lower()}')


# Replace the word in the sentence with a new word of your choice.
print(sentence.replace(word, 'coffe'))

# Print the last character of the sentence.
print(f'the last character of the sentence: {sentence[-1]}')