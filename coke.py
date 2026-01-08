amount_due = 50
coins = [5, 10, 25]

while True:
    insert_coin = int(input("Insert Coin: "))

    if insert_coin in coins:
        amount_due -= insert_coin

    if amount_due > 0:
        print("Amount Due:", amount_due)
    else:
        print("Change Owed:", abs(amount_due))
        break






