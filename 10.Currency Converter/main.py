import requests

# Offline fallback exchange rates (USD base)
OFFLINE_RATES = {
    "USD": 1.0,
    "EUR": 0.94,
    "GBP": 0.80,
    "LKR": 300.50,
    "JPY": 147.20,
    "AUD": 1.55
}


def get_rates():
    """Try fetching live rates, otherwise use offline fallback."""
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url, timeout=5)
        data = response.json()
        if response.status_code == 200 and "rates" in data:
            print("✅ Using live exchange rates")
            return data["rates"]
    except:
        pass

    print("⚠️ Using offline rates (no internet or API error)")
    return OFFLINE_RATES


def convert_currency(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another."""
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Unsupported currency code.")

    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return converted


def main():
    rates = get_rates()
    print("Welcome to Currency Converter 💱")
    print("Available currencies:", ", ".join(sorted(list(rates.keys())[:10])) + ", ...")

    while True:
        try:
            from_curr = input("\nFrom currency (e.g., USD, EUR, LKR) or 'q' to quit: ").upper()
            if from_curr == "Q":
                break

            to_curr = input("To currency: ").upper()
            amount = float(input("Amount: "))

            result = convert_currency(amount, from_curr, to_curr, rates)
            print(f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")

        except ValueError as e:
            print("Error:", e)
        except Exception:
            print("Something went wrong. Try again.")

    print("Thanks for using Currency Converter!")


if __name__ == "__main__":
    main()
