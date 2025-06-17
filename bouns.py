
sentence = "Chelsea is the best club in London, they have two champions league between all clubs in London"
word = "London"


print(f"The length of the sentence: {len(sentence)}")
print(f"Index of the first occurrence: {sentence.find(word)}")
print(f"The number of times the word appears: {sentence.count(word)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Uppercase: {sentence.lower()}")
print(f"Replace: {sentence.replace(word, 'England')}")
print(f"The last character in the sentence: {sentence[-1]}")

