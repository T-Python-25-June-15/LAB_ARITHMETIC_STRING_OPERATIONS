#bonus lab (wasan alqahtani)

#Define a string variable containing a sentence with at least 10 words.
welcoming_sentence = "Hello I am is Wasan Alqahtani I studied information technology and I am passionate in technology"

#Define a string variable containing a word that appears in the sentence.
word = "am"

#Print the length of the sentence.
print(len(welcoming_sentence))

#Print the index of the first occurrence of the word in the sentence.
print(welcoming_sentence.find(word))

#Print the number of times the word appears in the sentence.
print(welcoming_sentence.count(word))

#Print the sentence in all uppercase letters.
print(welcoming_sentence.upper())

#Print the sentence in all lowercase letters.
print(welcoming_sentence.lower())

#Replace the word in the sentence with a new word of your choice.
new_sentence = welcoming_sentence.replace(word,"'m")

#Print the last character of the sentence.
print(welcoming_sentence[-1])