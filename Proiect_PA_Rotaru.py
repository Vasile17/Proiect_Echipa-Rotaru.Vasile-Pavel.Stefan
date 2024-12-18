import tkinter as tk

# Funcții de conversie
def hex_to_decimal():
    hex_value = entry_hex.get()
    try:
        decimal_value = int(hex_value, 16)
        entry_decimal.delete(0, tk.END)
        entry_decimal.insert(0, str(decimal_value))
        entry_decimal.config(bg="lightgreen")  # Culoare verde pentru validitate
    except ValueError:
        entry_decimal.delete(0, tk.END)
        entry_decimal.insert(0, "Invalid Input")
        entry_decimal.config(bg="red")  # Culoare roșie pentru eroare

def hex_to_binary():
    hex_value = entry_hex.get()
    try:
        decimal_value = int(hex_value, 16)
        binary_value = bin(decimal_value)[2:]  # elimină prefixul '0b'
        entry_binary.delete(0, tk.END)
        entry_binary.insert(0, binary_value)
        entry_binary.config(bg="lightgreen")  # Culoare verde pentru validitate
    except ValueError:
        entry_binary.delete(0, tk.END)
        entry_binary.insert(0, "Invalid Input")
        entry_binary.config(bg="red")  # Culoare roșie pentru eroare

def decimal_to_hex():
    decimal_value = entry_decimal.get()
    try:
        decimal_value = int(decimal_value)
        hex_value = hex(decimal_value)[2:]  # elimină prefixul '0x'
        entry_hex.delete(0, tk.END)
        entry_hex.insert(0, hex_value.upper())
        entry_hex.config(bg="lightgreen")  # Culoare verde pentru validitate
    except ValueError:
        entry_hex.delete(0, tk.END)
        entry_hex.insert(0, "Invalid Input")
        entry_hex.config(bg="red")  # Culoare roșie pentru eroare

def decimal_to_binary():
    decimal_value = entry_decimal.get()
    try:
        decimal_value = int(decimal_value)
        binary_value = bin(decimal_value)[2:]  # elimină prefixul '0b'
        entry_binary.delete(0, tk.END)
        entry_binary.insert(0, binary_value)
        entry_binary.config(bg="lightgreen")  # Culoare verde pentru validitate
    except ValueError:
        entry_binary.delete(0, tk.END)
        entry_binary.insert(0, "Invalid Input")
        entry_binary.config(bg="red")  # Culoare roșie pentru eroare

def binary_to_decimal():
    binary_value = entry_binary.get()
    try:
        decimal_value = int(binary_value, 2)
        entry_decimal.delete(0, tk.END)
        entry_decimal.insert(0, str(decimal_value))
        entry_decimal.config(bg="lightgreen")  # Culoare verde pentru validitate
    except ValueError:
        entry_decimal.delete(0, tk.END)
        entry_decimal.insert(0, "Invalid Input")
        entry_decimal.config(bg="red")  # Culoare roșie pentru eroare

def binary_to_hex():
    binary_value = entry_binary.get()
    try:
        decimal_value = int(binary_value, 2)
        hex_value = hex(decimal_value)[2:]  # elimină prefixul '0x'
        entry_hex.delete(0, tk.END)
        entry_hex.insert(0, hex_value.upper())
        entry_hex.config(bg="lightgreen")  # Culoare verde pentru validitate
    except ValueError:
        entry_hex.delete(0, tk.END)
        entry_hex.insert(0, "Invalid Input")
        entry_hex.config(bg="red")  # Culoare roșie pentru eroare

# Crearea ferestrei principale
root = tk.Tk()
root.title("Hex - Decimal - Binary Conversions")
root.geometry("450x300")  # Dimensiunea ferestrei

# Crearea elementelor de interfață
label_hex = tk.Label(root, text="Hex:")
label_hex.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_hex = tk.Entry(root, width=15)
entry_hex.grid(row=0, column=1, padx=10, pady=5, ipadx=10)

label_decimal = tk.Label(root, text="Dec:")
label_decimal.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_decimal = tk.Entry(root, width=15)
entry_decimal.grid(row=1, column=1, padx=10, pady=5, ipadx=10)

label_binary = tk.Label(root, text="Bin:")
label_binary.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_binary = tk.Entry(root, width=15)
entry_binary.grid(row=2, column=1, padx=10, pady=5, ipadx=10)

# Crearea butoanelor pentru conversie
button_hex_to_decimal = tk.Button(root, text="Hex -> Dec", command=hex_to_decimal)
button_hex_to_decimal.grid(row=0, column=2, padx=10, pady=5)

button_hex_to_binary = tk.Button(root, text="Hex -> Bin", command=hex_to_binary)
button_hex_to_binary.grid(row=0, column=3, padx=10, pady=5)

button_decimal_to_hex = tk.Button(root, text="Dec -> Hex", command=decimal_to_hex)
button_decimal_to_hex.grid(row=1, column=2, padx=10, pady=5)

button_decimal_to_binary = tk.Button(root, text="Dec -> Bin", command=decimal_to_binary)
button_decimal_to_binary.grid(row=1, column=3, padx=10, pady=5)

button_binary_to_decimal = tk.Button(root, text="Bin -> Dec", command=binary_to_decimal)
button_binary_to_decimal.grid(row=2, column=2, padx=10, pady=5)

button_binary_to_hex = tk.Button(root, text="Bin -> Hex", command=binary_to_hex)
button_binary_to_hex.grid(row=2, column=3, padx=10, pady=5)

# Start aplicația
root.mainloop()
