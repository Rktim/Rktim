
import tkinter as tk

def add(a, b):
    res = a + b
    output_label.config(text=f"Result: {res}")

def sub(a, b):
    res = a - b
    output_label.config(text=f"Result: {res}")

def multi(a, b):
    res = a * b
    output_label.config(text=f"Result: {res}")

def div(a, b):
    res = a / b
    output_label.config(text=f"Result: {res}")

root = tk.Tk()
root.title("Calculator.rk")
root.geometry('450x320')
root.configure(bg='pink')

label = tk.Label(root, text="Enter the first number:", bg='light blue', font='DejaVu')
label.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label = tk.Label(root, text="Enter the second number:", bg='light green', font='DejaVu')
label.pack()
entry_b = tk.Entry(root)
entry_b.pack()

output_label = tk.Label(root, text="Result: ", bg='purple', font='Ariel')
output_label.pack()

button = tk.Button(root, text=" + ", command=lambda: add(int(entry_a.get()), int(entry_b.get())), bg='orange')
button.pack()

button = tk.Button(root, text=" - ", command=lambda: sub(int(entry_a.get()), int(entry_b.get())), bg='green')
button.pack()

button = tk.Button(root, text=" x ", command=lambda: multi(int(entry_a.get()), int(entry_b.get())), bg='blue')
button.pack()

button = tk.Button(root, text=" / ", command=lambda: div(int(entry_a.get()), int(entry_b.get())), bg='yellow')
button.pack()

root.mainloop()
