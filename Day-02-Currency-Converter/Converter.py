import requests


def convert_currecy(amount, from_curr, to_curr):
    url = f"https://open.er-api.com/v6/latest/{from_curr.upper()}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if response.status_code == 200 and data.get("result") == "success":
            rates = data.get("rates", {})
            if to_curr.upper() in rates:
                converted_amount = amount * rates[to_curr.upper()]
                rate = rates[to_curr.upper()]
                return converted_amount, rate
            else:
                print(f"Error: Target currency '{to_curr}' not found in the exchange rates.")
                return None, None
        else:
            print("Error: Unable to fetch exchange rates.")
            return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None
def main():
    print("=" * 40)
    print("Currency Converter")
    print("=" * 40)

    try:
        amount = float(input("Enter the amount to convert: "))
        from_curr = input("Enter the source currency (e.g., USD, EUR, PKR, INR): ").strip()
        to_curr = input("Enter the target currency (e.g., USD, EUR, PKR, INR): ").strip()

        print(f"\nFetching exchange rates from {from_curr.upper()} to {to_curr.upper()}...")

        result, rate = convert_currecy(amount, from_curr, to_curr)
        if result is not None and rate is not None:
            print(f"\n{amount} {from_curr.upper()} = {result:.2f} {to_curr.upper()}")
            print(f"Exchange Rate: 1 {from_curr.upper()} = {rate:.4f} {to_curr.upper()}")
            print("=" * 35)

    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the amount.")


if __name__ == "__main__":
    main()
