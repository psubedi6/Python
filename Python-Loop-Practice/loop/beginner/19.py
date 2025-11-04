#Reverse a string using a loop.
word=input("Enter the character: ")
rev_word=""
for i in word:
    rev_word=i+rev_word
print(rev_word)