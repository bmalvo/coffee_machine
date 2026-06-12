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
# 5 Process coins
# 6 Check transaction successful
# 6.1 Offer change
# 7 Make coffee


def coffee_machine():
    not_broken = True
    water = 300 # 3000 max
    milk = 200 # 2000 max
    coffee = 100 # 1000 max
    money = 0
    pay = 0
    recipes = {
        'e': {
            'name': 'espresso',
            'water': 50,
            'coffee': 18,
            'milk': 0,
            'price': 1.50},
        'l': {
            'name': 'latte',
            'water': 200,
            'coffee': 24,
            'milk': 150,
            'price': 2.50},
        'c': {
            'name': 'cappuccino',
            'water': 250,
            'coffee': 24,
            'milk': 100,
            'price': 3.00}
    }
    coins = {
        'q': 0.25,
        'd': 0.10,
        'n': 0.05,
        'p': 0.01,
        'f': 0
    }
    while not_broken:
        coffee_type = input('What would you like? ([e]spresso/[l]atte/[c]appuccino): ')
        # print(recipes[coffee_type])
        if coffee_type in recipes:
            if water - recipes[coffee_type]['water'] < 0:
                print('Sorry there is not enough water.')
                break
            if coffee - recipes[coffee_type]['coffee'] < 0:
                print('Sorry there is not enough coffee.')
                break
            if milk - recipes[coffee_type]['milk'] < 0:
                print('Sorry there is not enough milk.')
                break
        if coffee_type == 'off':
            not_broken = False
        if coffee_type == 'report':
            print(f"""
            Water: {water}ml
            Milk: {milk}ml
            Coffee: {coffee}g
            Money: ${money}
            """)
            break
        # pay = 0
        coin = True
        print(f'''
        Please insert coins. ${recipes[coffee_type]['price']}
        Press "q" for quarter, "d" for dime, "n" for nickel,
        "p" for penni and "f" if You have finished                
        ''')
        while coin != 0:
            coin = input('insert coin: ')
            if coin in coins.keys():
                pay += coins[coin]
                print(f'coin {coins[coin]}')
                print(f'pay {pay}')
            else:
                print('Incorrect coin')
            if coin == 'f':
                break
        print(f'inserted coins: {pay}')
        if recipes[coffee_type]['price'] > pay:
            print("Sorry that's not enough money. Money refunded.")
            pay = 0
        else:
            if pay > recipes[coffee_type]['price']:
                change = round(pay - recipes[coffee_type]['price'] ,2)
                print(f'Here is ${change} dollars in change.')
                money = pay - change
                pay = 0
            water = water - recipes[coffee_type]['water']
            milk = milk - recipes[coffee_type]['milk']
            coffee = coffee - recipes[coffee_type]['coffee']
            print(f'Here is your {recipes[coffee_type]['name']}. Enjoy!')
    return

coffee_machine()
