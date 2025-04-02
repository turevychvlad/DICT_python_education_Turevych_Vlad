# Етап 1: простий конвертер в долари
print("--- Етап 1 ---")
mycoins = float(input("Please, enter the number of mycoins you have: > "))
rate_usd = float(input("Please, enter the exchange rate: > "))
usd_amount = round(mycoins * rate_usd, 2)
print(f"The total amount of dollars: {usd_amount}\n")

# Етап 2: конвертація в декілька валют
print("--- Етап 2 ---")
mycoins = float(input("> "))
exchange_rates = {
    'ARS': 0.82,
    'HNL': 0.17,
    'AUD': 1.9622,
    'MAD': 0.208
}
for currency, rate in exchange_rates.items():
    amount = round(mycoins * rate, 2)
    print(f"I will get {amount} {currency} from the sale of {mycoins} mycoins.")
print()

# Етап 3: отримаємо фактичні курси для USD та EUR
print("--- Етап 3 ---")
import requests

base_currency = input("Enter your currency code (e.g., AUD): ").lower()
url = f"http://www.floatrates.com/daily/{base_currency}.json"
response = requests.get(url)
data = response.json()

if 'usd' in data:
    print(f"USD rate: {data['usd']['rate']}")
if 'eur' in data:
    print(f"EUR rate: {data['eur']['rate']}\n")

# Етап 4: обмін з кешуванням
print("--- Етап 4 ---")
currency_from = input("Enter your base currency: ").lower()
url = f"http://www.floatrates.com/daily/{currency_from}.json"
currency_data = requests.get(url).json()

# створюємо кеш
cache = {}
if 'usd' in currency_data:
    cache['usd'] = currency_data['usd']
if 'eur' in currency_data:
    cache['eur'] = currency_data['eur']

while True:
    currency_to = input("\nEnter currency to convert to (or press enter to exit): ").lower()
    if currency_to == "":
        break
    amount = float(input("Enter amount to convert: "))
    print("Checking the cache...")

    if currency_to in cache:
        print("It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[currency_to] = currency_data.get(currency_to, None)

    rate_info = cache[currency_to]
    if rate_info is None:
        print("Sorry, rate info not available.\n")
        continue

    converted = round(amount * rate_info['rate'], 2)
    print(f"You received {converted} {currency_to.upper()}.")
