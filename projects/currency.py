import requests

fromCurrency = input("What currency to you want to convert from? ").upper()
toCurrency = input("What currency do you want to convert into? ").upper()
amount = float(input("How much do you want to convert? "))

currencyData = requests.get(f'https://api.frankfurter.app/latest?amount={amount}&from={fromCurrency}&to={toCurrency}')
if currencyData.status_code == 200:
    converted = currencyData.json()['rates'][toCurrency]

    print(f"{amount} {fromCurrency} is equal to {converted} {toCurrency}")
else:
    print("An error has an occured")

