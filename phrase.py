text = input("Please write the phrase to sort:\n")

text = text.split()
text.sort()

for word in text:
    print(word + "\n")