# Billing-System


Café Billing System
This Python script uses the Tkinter library to create a simple GUI application for a cafe billing system. The system allows users to input the quantities of different cafe items, calculates the subtotal, and generates a bill entry.

Prerequisites
Before running the script, ensure that you have the following:

Python installed on your system.
The necessary Python libraries (tkinter, pandas) installed. You can install them using the following command:
bash
Copy code
pip install pandas
Getting Started
Clone the repository or download the script.
Ensure that the required CSV files (Pricing.csv and Bill.csv) are present in the specified directory (Files).
Usage
Run the script using the following command:

bash
Copy code
python cafe_billing_system.py
The GUI window will appear with labels for cafe items, entry fields for quantities, and a "Submit" button.

Features
Cafe Items: The script displays cafe items (Cafe Latte, Cappuccino, Espresso) and their positions on the GUI.

Entry Fields: Users can enter the quantities of each cafe item in the provided entry fields.

Submit Button: Clicking the "Submit" button triggers the gen function, which calculates the subtotal based on the entered quantities and updates the bill CSV file.

Error Handling: If an error occurs during the process, an error message is displayed in red.

Files
Pricing.csv: Contains the pricing information for cafe items.
Bill.csv: Stores the bill entries with date, subtotal, tax, and total.
Notes
Make sure to have the required CSV files in the specified directory before running the script.
The script uses the Tkinter library for the graphical user interface and Pandas for data manipulation.
Feel free to customize the script according to your needs or enhance its features.
