# code will be here

# 1 user input

def coffee_machine():
    coffee_type = input('What would you like? ([e]spresso/[l]atte/[c]appuccino): ')
    return print(coffee_type)

not_broken = True

while not_broken:
    coffee_machine()
