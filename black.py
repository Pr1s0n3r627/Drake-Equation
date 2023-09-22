import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        R = float(entry_R.get())
        p = float(entry_p.get())
        n = float(entry_n.get())
        f = float(entry_f.get())
        i = float(entry_i.get())
        c = float(entry_c.get())
        L = float(entry_L.get())

        N = R * p * n * f * i * c * L
        result_label.config(text=f"The estimated number of active Alien civilizations is: {N:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values in all fields.")

# Create the main window
window = tk.Tk()
window.title("Drake Equation Calculator")
window.configure(bg="#1E1E1E")  # Dark background color

# Create a custom style for labels and entries
style = ttk.Style()
style.configure("TLabel", foreground="#D9D9D9", background="#1E1E1E", font=("Arial", 16))
style.configure("TEntry", foreground="#D9D9D9", background="black", font=("Arial", 16))  # Input fields are black
style.configure("TButton", foreground="black", font=("Arial", 16))  
# Button text color is black, no neon here

# Create and arrange input fields and labels using the grid layout
labels = ["Rate of creation of stars:", "Percentage of stars with planets:", "Fraction of planets in Goldilocks zone:",
          "Fraction of planets where life can develop:", "Fraction of planets with intelligent life:",
          "Fraction of planets where life is willing and able to communicate:", "Expected lifetime in years:"]

for row, label_text in enumerate(labels):
    label = ttk.Label(window, text=label_text)
    label.grid(row=row, column=0, sticky=tk.W, padx=10, pady=10)

entry_R = ttk.Entry(window)
entry_p = ttk.Entry(window)
entry_n = ttk.Entry(window)
entry_f = ttk.Entry(window)
entry_i = ttk.Entry(window)
entry_c = ttk.Entry(window)
entry_L = ttk.Entry(window)

entry_R.grid(row=0, column=1, padx=10, pady=10)
entry_p.grid(row=1, column=1, padx=10, pady=10)
entry_n.grid(row=2, column=1, padx=10, pady=10)
entry_f.grid(row=3, column=1, padx=10, pady=10)
entry_i.grid(row=4, column=1, padx=10, pady=10)
entry_c.grid(row=5, column=1, padx=10, pady=10)
entry_L.grid(row=6, column=1, padx=10, pady=10)

calculate_button = ttk.Button(window, text="Calculate", command=calculate, style="TButton")
calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

result_label = ttk.Label(window, text="", font=("Arial", 20, "bold"), foreground="#D9D9D9", background="#1E1E1E")
result_label.grid(row=8, column=0, columnspan=2, pady=20)

window.mainloop()
