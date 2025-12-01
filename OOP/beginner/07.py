#Write code that shows method overriding (child class overrides parent method).
class Car:
    def brand(self):
        print("Mercedez benz")
    
class Toyota(Car):
    def brand(self):
        print("Toyota corolla")

c= Car()
t= Toyota()

c.brand()
t.brand()