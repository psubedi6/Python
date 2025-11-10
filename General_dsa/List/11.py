#Create a dictionary of three friends and their phone numbers. Use:
#keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them
my_dict={
    "Prakash":4234324234,
    "Prinshu":432432432,
    "Diana":423443242
}
print(my_dict.keys())
print(my_dict.values())
print(my_dict)
for keys,values in (my_dict.items()):
    print(keys,values)