import requests

def currency_converter(amount, convert_currency):
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        if convert_currency not in data['rates']:
            raise ValueError("Invalid currency code!")
        convert_currency_rates = data['rates'][convert_currency]
        converted_amount = amount * convert_currency_rates
        return converted_amount
    else:
        raise Exception("Data not found")

def main():
    try:
        amount = float(input("Enter a USD amount: "))
        convert_currency = input("Enter the currency to convert in: ")
        converted_amount = currency_converter(amount, convert_currency.upper())
        print(f"Converted currency is {converted_amount}")

    except ValueError as e:
        print(f"Error: {e}")

    except requests.exceptions.RequestException:
        print("Error: Unable to fetch exchange rates. Check your internet connection.")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
