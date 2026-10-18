
import csv


class ExchangeRates:
    def __init__(self, filename):
        self.filename = filename
        self.usd_cad_rate = self.read_exchange_rate()

    def read_exchange_rate(self):
        with open(self.filename, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Find the column containing the USD/CAD exchange rate
        for i, row in enumerate(rows):
            headers = [item.strip() for item in row]

            rate_column = None

            for j, header in enumerate(headers):
                if header.upper() == "FXAUSDCAD":
                    rate_column = j
                    break

            if rate_column is not None:
                # Find the latest valid exchange rate, starting at the bottom
                for data_row in reversed(rows[i + 1:]):
                    if len(data_row) > rate_column:
                        try:
                            return float(data_row[rate_column])
                        except ValueError:
                            continue

        raise ValueError(
            "Could not find a valid FXAUSDCAD exchange rate in the CSV file."
        )

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in ("USD", "CAD") or to_currency not in ("USD", "CAD"):
            raise ValueError("Currencies must be USD or CAD.")

        if from_currency == to_currency:
            return amount

        elif from_currency == "USD" and to_currency == "CAD":
            return amount * self.usd_cad_rate

        else:  # CAD to USD
            return amount / self.usd_cad_rate


# Main program
filename = "BankOfCanadaExchangeRate.2026.csv"

try:
    exchange = ExchangeRates(filename)

    print("USD/CAD Exchange Rate:", exchange.usd_cad_rate)

    amount = float(input("Enter the amount: "))
    from_currency = input("Convert from (USD or CAD): ").strip().upper()
    to_currency = input("Convert to (USD or CAD): ").strip().upper()

    result = exchange.convert(amount, from_currency, to_currency)

    print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

except ValueError as error:
    print("Error:", error)

except FileNotFoundError:
    print("Error: CSV file not found. Check the filename and folder.")
