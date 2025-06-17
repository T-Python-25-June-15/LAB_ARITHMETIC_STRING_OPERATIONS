sentence= "my name is lujain saleh alaamri i love python and java"
word="python"
print(f"length: {len(sentence)}")
print(f"frist word: '{word}': {sentence.find (word)}")
print(f"number of word: '{word}': {sentence.count(word)}")
print("uppercase: ",sentence.upper())
print("lowercase: ",sentence.lower())
new_sentence=sentence.replace(word,"java")
print("new sentence: ",new_sentence)
print("last charachter: ",sentence[-1])