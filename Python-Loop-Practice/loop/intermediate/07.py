#Check if a string is a palindrome.
word=input("Enter the word: ")
rev_word=""
for i in word:
    rev_word=i+rev_word
if(rev_word==word):
    print("It is a palindrome word")
else:
    print("It is not a palindrome word")