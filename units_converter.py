'''Using sys.exit() for a converter finishing'''
import sys

# The 1-st element is a list is a coefficient for conversion
# from this currency to USD, 2-nd - coefficient for conversion
# from USD to this currency. The last two elements are for nice output

currency = {
    "NOK": [0.1162841, 8.5996282, "Norwegian Krone", "Norwegian Kroner"],
    "SEK": [0.11489732, 8.7051764, "Swedish Krona", "Swedish Kronor"],
    "EUR": [1.1698031, 0.8548176, "Euro", "Euros"],
    "ISK": [0.0078147443, 127.96324, "Iceland Krona", "Icelandic Kronur"],
    "DKK": [0.15731544, 6.3568108, "Danish Krone", "Danish Kroner"]
}


def currency_check():
    '''Function for correct currency checkout'''
    local_var = input("Enter a currency: ").upper()
    if local_var == 'STOP':
        sys.exit()
    count = 0
    while count != 1:
        if local_var in currency:
            return local_var
        print("It's not an available currency. ", end="")
        local_var = input("Choose a currency among listed above: ").upper()
        if local_var == "STOP":
            sys.exit()


def amount_check():
    '''Function for amount checkout'''
    local_var = input("Enter an amount of money: ")
    if local_var == 'stop':
        sys.exit()
    count = 0
    while count != 1:
        try:
            float(local_var)
            return float(local_var)
        except ValueError:
            local_var = input("Please, enter a valid amount: ")
            if local_var == 'stop':
                sys.exit()


print("Here is a scandinavian currency converter, that is available for\n"
      "the following currencies:\n"
      " - Norwegian krone (NOK),\n"
      " - Swedish krona (SEK),\n"
      " - Danish krone (DKK),\n"
      " - Iceland krona (ISK),\n"
      " - Euro (EUR).\n"
      "Enter the three-letter currency code (letter case is not important),\n"
      "and an amount of money. Enter 'stop' to finish the converter.\n")
VAR = None
while VAR != 1:
    currency_1 = currency_check()
    amount = amount_check()
    while amount <= 0:
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
            final_amount = round(amount * currency.get(currency_1)[0]
                                 * currency.get(key)[1], 2)
            if final_amount == 1:
                print("\t", final_amount, currency.get(key)[2])
            elif final_amount != 1:
                print("\t", final_amount, currency.get(key)[3])
    print("================\nOne more conversion? Remember, that ", end="")
    print("the available currencies are:\n"
          "Norwegian krone (NOK), Swedish krona (SEK), Danish krone (DKK),\n"
          "Iceland krona (ISK), and Euro (EUR).\n"
          "Or enter 'stop' to finish the converter.\n")
