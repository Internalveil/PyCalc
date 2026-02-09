import tkinter as tk

# Main window
root = tk.Tk()
root.title("Shaftys' Calculator")
root.geometry("400x500")
root.resizable(False, False)

# -------------------------------
# Display at top
# -------------------------------
display = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Bind Enter key to calculate
display.bind("<Return>", lambda event: calculate())

# -------------------------------
# Functions
# -------------------------------
def add_to_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

def calculate():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# -------------------------------
# Top buttons row (row 1): C, ←, /, *
# -------------------------------
tk.Button(root, text='C', width=5, height=2, font=("Arial", 18),
          command=clear, bg="#ff4500").grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text='←', width=5, height=2, font=("Arial", 18),
          command=backspace, bg="#ff6347").grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text='/', width=5, height=2, font=("Arial", 18),
          command=lambda: add_to_display('/'), bg="#ffd700").grid(row=1, column=2, padx=5, pady=5)
tk.Button(root, text='*', width=5, height=2, font=("Arial", 18),
          command=lambda: add_to_display('*'), bg="#ffd700").grid(row=1, column=3, padx=5, pady=5)

# -------------------------------
# Numbers and operators
# -------------------------------
buttons = [
    ('7', '8', '9', '-'),
    ('4', '5', '6', '+'),
    ('1', '2', '3', '='),  # = in middle row
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '=':
            tk.Button(root, text='=', width=5, height=2, font=("Arial", 18),
                      command=calculate, bg="#32cd32").grid(row=i+2, column=j, padx=5, pady=5)
        elif text in '+-':
            tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      command=lambda t=text: add_to_display(t), bg="#ffd700").grid(row=i+2, column=j, padx=5, pady=5)
        else:
            tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                      command=lambda t=text: add_to_display(t), bg="#f0f0f0").grid(row=i+2, column=j, padx=5, pady=5)

# -------------------------------
# Bottom row: 0 and .
# -------------------------------
tk.Button(root, text='0', width=11, height=2, font=("Arial", 18),
          command=lambda: add_to_display('0'), bg="#f0f0f0").grid(row=5, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text='.', width=5, height=2, font=("Arial", 18),
          command=lambda: add_to_display('.'), bg="#f0f0f0").grid(row=5, column=2, padx=5, pady=5)


root.mainloop()
