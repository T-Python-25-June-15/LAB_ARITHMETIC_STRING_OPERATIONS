sentence:str = "Don't be sad about your failure as long as you are trying to get up again"
word:str = "sad"

print(f"the length of the sentence is: {len(sentence)}")
print(f"the index of the first occurrence of the word in the sentence is: {sentence.find(word)}")
print(f"the number of times the word appears in the sentence is: {sentence.count(word)}")
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(word, "worry"))
print(sentence[-1])