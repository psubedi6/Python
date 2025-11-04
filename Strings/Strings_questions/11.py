#Write a program that counts how many vowels are in a given string
a=input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count=0

for i in vowels:
    count+= a.count(i)
print(count)