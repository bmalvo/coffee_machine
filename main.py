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
# 3 print report
# 4 Check resources sufficient


def coffee_machine():
    not_broken = True
    water = 30 # 3000 max
    milk = 200 # 2000 max
    coffee = 100 # 1000 max
    money = 0
    recipes = {
        'e': {
        'water': 50,
        'coffee': 18,
        'milk': 0,
        'price': 1.50},
        'l': {
            'water': 200,
            'coffee': 24,
            'milk': 150,
            'price': 2.50},
        'c': {
            'water': 250,
            'coffee': 24,
            'milk': 100,
            'price': 3.00}
    }
    while not_broken:
        coffee_type = input('What would you like? ([e]spresso/[l]atte/[c]appuccino): ')
        print(recipes[coffee_type])
        if coffee_type in recipes:
            if water - recipes[coffee_type]['water'] < 0:
                print('Sorry there is not enough water.')
                not_broken = False
            if coffee - recipes[coffee_type]['coffee'] < 0:
                print('Sorry there is not enough coffee.')
                not_broken = False
            if milk - recipes[coffee_type]['milk'] < 0:
                print('Sorry there is not enough milk.')
                not_broken = False
        if coffee_type == 'off':
            not_broken = False
        if coffee_type == 'report':
            print(f"""
            Water: {water}ml
            Milk: {milk}ml
            Coffee: {coffee}g
            Money: ${money}
            """)
    return

coffee_machine()
