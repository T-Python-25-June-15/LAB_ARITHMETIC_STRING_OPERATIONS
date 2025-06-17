sentense:str = "im meshari alharbi software engineering student at king saud university"
word:str = "meshari"

print("length of sentense: " + str(len(sentense)))
print("\n index of first occurrence of word: " + str(sentense.index(word)))
print("\n number of times word appears in sentense: " + str(sentense.count(word)))
print("\n sentense upercase: " + sentense.upper())
print("\n sentense lowercase: " + sentense.lower())
print("\n new word: " +sentense.replace(word, "mohammed"))
print('\n last charact: ' + sentense[-1])
