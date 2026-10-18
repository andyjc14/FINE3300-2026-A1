class ExchangeRates:
    def __init__(self, filename):
        # open file, read every row into a list, close file
        file = open(filename)
        lines = file.readlines()
        file.close()

        # split first row of column names into a list
        header = lines[0].split(",")
        # find position of USD/CAD column
        column = header.index("FXAUSDCAD")

        # last row contains the latest exchange rate, split into a list
        last_row = lines[len(lines) - 1].split(",")
        # pick value from USD/CAD column and store value as a float 
        self.__last_rate = float(last_row[column])

    def convert(self, amount, from_currency, to_currency):
        # if USD to CAD, multiply amount by rate
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.__last_rate
        # if CAD to USD, divide amount by rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.__last_rate

# create object
rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

# prompt user for amount and currencies
amount = float(input("Enter the desired amount to convert: "))
# .upper is used to remove case sensitivity 
from_currency = input("Convert from (choose USD or CAD): ").upper()
to_currency = input("Convert to (choose USD or CAD): ").upper()

result = rates.convert(amount, from_currency, to_currency)
# format amount and result to strings for output, rounded to 2 decimal places
amount_text = str(round(amount, 2))
result_text = str(round(result, 2))

print("$" + amount_text, from_currency, "is equal to $" + result_text, to_currency + ".")
                
                