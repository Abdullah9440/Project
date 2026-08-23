#without using API 
def convert(amount, rate):
    return amount * rate


rates = {
    "USD": 120,
    "INR": 1.40,
    "EUR": 140,
    "BDT": 1
}

amount = float(input("Enter amount: "))
from_currency = input("From currency (USD/INR/EUR/BDT): ").upper()
to_currency = input("To currency (USD/INR/EUR/BDT): ").upper()

if from_currency in rates and to_currency in rates:
    result = amount * rates[from_currency] / rates[to_currency]

    print(amount, from_currency, "=", result, to_currency)
else:
    print("Invalid currency")