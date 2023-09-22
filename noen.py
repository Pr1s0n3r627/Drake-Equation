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

# the main window
window = tk.Tk()
window.title("Drake Equation Calculator")

# Dark mode and neon-colored theme
window.configure(bg="#111")
style = ttk.Style()
style.configure("TLabel", foreground="#FF00FF", background="#111", font=("Arial", 12))
style.configure("TEntry", foreground="#00FFFF", background="#333", font=("Arial", 12))
style.configure("TButton", foreground="#00FF00", background="#222", font=("Arial", 12))
style.configure("TLabel", foreground="#FF00FF")
style.map("TButton", foreground=[('active', '#00FF00')])

# Create and arrange input fields and labels using the grid layout
labels = ["Rate of creation of stars:",
            "Percentage of stars with planets:",
            "Fraction of planets in Goldilocks zone:",
            "Fraction of planets where life can develop:",
            "Fraction of planets with intelligent life:",
            "Fraction of planets where life is willing and able to communicate:",
            "Expected lifetime in years:"]

for row, label_text in enumerate(labels):
    label = ttk.Label(window, text=label_text)
    label.grid(row=row, column=0, sticky=tk.W, padx=10, pady=5)

entry_R = ttk.Entry(window)
entry_p = ttk.Entry(window)
entry_n = ttk.Entry(window)
entry_f = ttk.Entry(window)
entry_i = ttk.Entry(window)
entry_c = ttk.Entry(window)
entry_L = ttk.Entry(window)

entry_R.grid(row=0, column=1, padx=10, pady=5)
entry_p.grid(row=1, column=1, padx=10, pady=5)
entry_n.grid(row=2, column=1, padx=10, pady=5)
entry_f.grid(row=3, column=1, padx=10, pady=5)
entry_i.grid(row=4, column=1, padx=10, pady=5)
entry_c.grid(row=5, column=1, padx=10, pady=5)
entry_L.grid(row=6, column=1, padx=10, pady=5)

calculate_button = ttk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

result_label = ttk.Label(window, text="", font=("Arial", 14, "bold"))
result_label.grid(row=8, column=0, columnspan=2, pady=10)

window.mainloop()
