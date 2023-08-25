import tkinter as tk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

def convert_currency():
    try:
        amount = float(amount_entry.get())
        source_currency = source_currency_var.get()
        target_currency = target_currency_var.get()
        
        c = CurrencyRates()
        exchange_rate = c.get_rate(source_currency, target_currency)
        
        converted_amount = amount * exchange_rate
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {target_currency}")
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

root = tk.Tk()
root.title("Currency Converter")

amount_label = tk.Label(root, text="Enter amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

source_currency_label = tk.Label(root, text="Select source currency:")
source_currency_label.pack()

source_currency_var = tk.StringVar()
source_currency_dropdown = tk.OptionMenu(root, source_currency_var, "USD", "EUR", "JPY", "GBP", "AUD")
source_currency_dropdown.pack()

target_currency_label = tk.Label(root, text="Select target currency:")
target_currency_label.pack()

target_currency_var = tk.StringVar()
target_currency_dropdown = tk.OptionMenu(root, target_currency_var, "USD", "EUR", "JPY", "GBP", "AUD")
target_currency_dropdown.pack()

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
