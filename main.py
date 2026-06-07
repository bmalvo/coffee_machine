# code will be here
# ingredients capacity: 3000ml - water, 2000ml - milk, 1000g - coffee
#  recipes:
#   espresso :
#         50ml - water
#         18g - cofee
#         $1.50 - cost
#   late :
#         200ml - water
#         24g - cofee
#         150ml - milk
#         $2.50 - cost
#   cappuccino :
#         250ml - water
#         24g - cofee
#         100ml - milk
#         $3.00 - cost

# 1 user input
# 2 build 'off' button


def coffee_machine():
    not_broken = True
    water = 300 # 3000 max
    milk = 200 # 2000 max
    coffee = 100 # 1000 max
    while not_broken:
        coffee_type = input('What would you like? ([e]spresso/[l]atte/[c]appuccino): ')
        print(coffee_type)
        if coffee_type == 'off':
            not_broken = False
    return

coffee_machine()