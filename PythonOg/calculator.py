import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        label_result.config(text=f"Result: {result}")
    except Exception:
        label_result.config(text="Error!")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")

# Input field
entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

# Button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack(pady=5)

# Result label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14))
label_result.pack(pady=10)

# Run the application
root.mainloop()
