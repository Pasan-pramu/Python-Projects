import requests

def get_exchange_rate(base, target):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    response = requests.get(url)
    data = response.json()
    return data["rates"].get(target)

def main():
    print("💱 Currency Converter")
    base = input("Enter base currency (e.g., USD): ").upper()
    target = input("Enter target currency (e.g., EUR): ").upper()
    amount = float(input("Enter amount: "))

    rate = get_exchange_rate(base, target)
    if rate:
        converted = amount * rate
        print(f"\n✅ {amount} {base} = {converted:.2f} {target}")
    else:
        print("❌ Invalid currency code.")

if __name__ == "__main__":
    main()
