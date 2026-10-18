# FINE3300-2026-A1
Assignment 1 - Andy Chung
Professor Habib
October 19, 2026

## Description
This project was building an exchange rate calculator in Python that converts to/from USD and CAD from the users input. The code uses course concepts such as Classes, Constructors, Methods as well as supplemental concepts from online forums, used to clarify syntax and other properties of the code.

## Files
The first file "ExchangeRates.py" was the calculator I built. I built it around the class, "ExchangeRates". The __init__ constructor runs automatically when an object of this class is created. The __init__ method opens the file, reads every row and then closes the file. I then used .split to split the entire first row to locate "FXAUSDCAD," and the last row which contains the most recent exchange rate. That value is located and stored. Then using the "convert" method, it calculates the conversion based on the direction the user wants (multiply for from CAD, divide for to CAD). It then defines an object "rates" and prompts the user to enter the amount and direction of conversion. The result is then printed with proper formatting. (Refer to documentation within code)

## How to run
1. Enter amount
2. Choose direction of conversion (from/to USD/CAD)





