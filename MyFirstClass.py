class Recipe():
    def __init__(self, dish, items,time) -> None:
        self.dish = dish
        self.items = items
        self.time = time
    
    def contents(self):
        print("The " + self.dish + " dish has " + str(self.items) + \
            " and takes " + str(self.time) + " mins to prepare")        

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["cheese","sauce"], 55)


print(pizza.items)
print(pasta.items)

print(pasta.contents())