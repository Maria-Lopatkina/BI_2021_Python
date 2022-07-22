import sys

currency = {
    "NOK": [0.1162841, 8.5996282, "Norwegian Krone", "Norwegian Kroner"],
    "SEK": [0.11489732, 8.7051764, "Swedish Krona", "Swedish Kronor"],
    "EUR": [1.1698031, 0.8548176, "Euro", "Euros"],
    "ISK": [0.0078147443, 127.96324, "Iceland Krona", "Icelandic Kronur"],
    "DKK": [0.15731544, 6.3568108, "Danish Krone", "Danish Kroner"]
}


def currency_check():  # to be sure, that the user chose the correct 1st currency
    x = input("Enter a currency for conversion: ").upper()
    if x == 'STOP':
        sys.exit()
    z = 0
    while z != 1:
        if x in currency:
            return x
        else:
            print("It's not an available currency. Please, choose a currency among listed above: ", end="")
            x = input().upper()
            if x == "STOP":
                sys.exit()


def amount_check():  # to be sure, that amount of money is a number
    x = input("Enter an amount of money: ")
    if x == 'stop':
        sys.exit()
    z = 0
    while z != 1:
        try:
            float(x)
            return float(x)
        except ValueError:
            x = input("Please, enter a valid amount: ")
            if x == 'stop':
                sys.exit()


print("Here is a scandinavian currency converter, that is available for the following currencies:\n"
      " - Norwegian krone (NOK),\n"
      " - Swedish krona (SEK),\n"
      " - Danish krone (DKK),\n"
      " - Iceland krona (ISK),\n"
      " - Euro (EUR).\n"
      "To convert, enter the three-letter currency codes (letter case is not important), then enter the amount.\n"
      "Enter 'stop' to finish the converter.\n")
x = None
while x != 1:
    currency_1 = currency_check()
    amount = amount_check()
    while not amount > 0:
        if amount < 0:
            print("The amount of money should be a positive number. ", end="")
            amount = amount_check()
        elif amount == 0:
            print("Please, choose an amount greater than 0. ", end="")
            amount = amount_check()
    if amount == 1:
        print(amount, currency.get(currency_1)[2], "equals:")
    elif amount != 1:
        print(amount, currency.get(currency_1)[3], "equals:")
    for key in currency:
        if key != currency_1:
            final_amount = round(amount * currency.get(currency_1)[0] * currency.get(key)[1], 2)
            if final_amount == 1:
                print("\t", final_amount, currency.get(key)[2])
            elif final_amount != 1:
                print("\t", final_amount, currency.get(key)[3])
    print("==============================\n\nOne more conversion? ", end="")
