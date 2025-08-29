class Chocolate:
    number_of_chocolates = 5
    name = "Kopiko"
    def introuduction(self):
        print("My fav chocolate is")
    def details(self):
        print("My fav chocolate is", self.name)
        print("I have theese number of chocolates", self.number_of_chocolates)

o = Chocolate()
o.introuduction() 
o.details()       