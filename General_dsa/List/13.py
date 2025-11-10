#Given a dictionary of products and their prices, find the product with the highest price.
mydict={
    "candy":10,
    "chips":4,
    "oats":8,
    "protein":60,
    "apple":2,
    "ball":3,
    "charge":4
}
max_p= max(mydict, key=mydict.get)
print("The highest price of an item is: ",max_p )