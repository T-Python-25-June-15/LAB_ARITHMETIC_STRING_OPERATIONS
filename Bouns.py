sentnce = "My name is Abdullah Alsofayan, i am 20 years old living in Riyadh, i study Computer Science in King Saud University and I've just completed my third year in university."

word = "Abdullah Alsofayan"
print("The length of the sentnce: ", len(sentnce))
print("")
print("Index of the word:", sentnce.find(word))
print("")

print("Number of times the word appears", sentnce.count(word))
print("")

print("UpperCase:",sentnce.upper())
print("")

print("LowerCase:",sentnce.lower())
print("")

new_word = "Mohammed"

sentnce = sentnce.replace(word,new_word)

print(sentnce)
print("")

print(sentnce[-1])