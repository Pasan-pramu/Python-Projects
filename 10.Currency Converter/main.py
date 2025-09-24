import requests

def get_exchange_rate(base, target):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if target not in data["rates"]:
            print("❌ Invalid target currency code.")
            return None

        return data["rates"][target]
    except Exception as e:
        print("⚠️ Error fetching exchange rate:", e)
        return None

def main():
    print("💱 Currency Converter")
    base = input("Enter base currency (e.g., USD): ").upper()
    target = input("Enter target currency (e.g., EUR): ").upper()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount.")
        return

    rate = get_exchange_rate(base, target)
    if rate:
        converted = amount * rate
        print(f"\n✅ {amount} {base} = {converted:.2f} {target}")

if __name__ == "__main__":
    main()
