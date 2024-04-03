menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "ameriicano"]

# def find_coffee(coffee, t = str(input('Input: c'))):

#     if coffee[0] == t:
#         return coffee
    
# map_coffee = map(find_coffee, menu)
# print(map_coffee)

# for x in map_coffee:
#     print(x)

# filtered_coffee = filter(find_coffee, menu)
# print(filtered_coffee)
# for x in filtered_coffee:
#     print(x)
    
    
# n + sum(n-1)

# n = 5 

# 5 + sum(5-1) == 9
# 4 + sum(4-1) == 3
# 3 + sum(3-1) == 2
# 2 + sum(2-1) == 1 returns 0

# 0 returned because n = 1

#  total 9 + 3 + 2 = 14

def sum(n):
    if n == 1:
        return 0
    return n + sum(n-1)

a = sum(5)
print(a)