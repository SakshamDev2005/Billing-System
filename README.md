# Billing-System


# Cafe Billing System:

This Python script uses the Tkinter library to create a simple GUI application for a cafe billing system. The system allows users to input the quantities of different cafe items, calculates the subtotal, and generates a bill entry.


# Perquisites:

Before running the script, ensure that you have the following:

Python installed on your system.

The necessary Python libraries (tkinter, pandas) installed.

You can install them using the following command - pip install pandas


# Getting Started:

Clone the repository or download the script.

Ensure that the required CSV files (Pricing.csv and Bill.csv) are present in the specified directory (Files).


# Usage:

Run the script using the following command: python cafe_billing_system.py

The GUI window will appear with labels for cafe items, entry fields for quantities, and a "Submit" button.


# Features:

1 - Cafe Items: The script displays cafe items (Cafe Latte, Cappuccino, Espresso) and their positions on the GUI.

2 - Entry Fields: Users can enter the quantities of each cafe item in the provided entry fields.

3 - Submit Button: Clicking the "Submit" button triggers the gen function, which calculates the subtotal based on the entered quantities and updates the bill CSV file.

4 - Error Handling: If an error occurs during the process, an error message is displayed in red.


# Files:

1 - Pricing.csv: Contains the pricing information for cafe items.

2 - Bill.csv: Stores the bill entries with date, subtotal, tax, and total.


# Notes:

1 -Make sure to have the required CSV files in the specified directory before running the script.

2 -The script uses the Tkinter library for the graphical user interface and Pandas for data manipulation.

3 - Feel free to customize the script according to your needs or enhance its features.
