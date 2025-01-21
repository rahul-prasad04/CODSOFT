import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid Input. Please try again.")

# Toggle light/dark mode
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

def apply_theme():
    if dark_mode:
        root.configure(bg="#1C2833")
        entry.configure(bg="#FDFEFE", fg="#1C2833")
        theme_button.configure(text="    ☀️", bg="#34495E", fg="white")
    else:
        root.configure(bg="#FDFEFE")
        entry.configure(bg="#1C2833", fg="#FDFEFE")
        theme_button.configure(text="🌙", bg="#E74C3C", fg="white")
    update_button_colors()

def update_button_colors():
    for btn in buttons:
        if dark_mode:
            btn.configure(bg="#34495E", fg="white", activebackground="#1ABC9C")
        else:
            btn.configure(bg="#D5D8DC", fg="#34495E", activebackground="#A2D9CE")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("420x600")
root.resizable(False, False)

# Initialize theme
dark_mode = True

# Entry widget for input and results
entry = tk.Entry(
    root, 
    font=("Arial", 24, "bold"), 
    bg="#FDFEFE", 
    fg="#1C2833", 
    justify="right", 
    bd=10, 
    relief=tk.FLAT
)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=10)

# Button layout
buttons = []
button_config = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

def create_button(text, command, row, col, colspan=1, wide=False):
    btn = tk.Button(
        root,
        text=text,
        font=("Arial", 18, "bold"),
        bg="#34495E" if dark_mode else "#D5D8DC",
        fg="white" if dark_mode else "#34495E",
        activebackground="#1ABC9C" if dark_mode else "#A2D9CE",
        activeforeground="white",
        bd=0,
        relief=tk.FLAT,
        width=10 if wide else 5,
        height=2,
        command=command
    )
    btn.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)
    #Hover effect
    def on_enter(event):
        btn.configure(bg="#1ABC9C")
    def on_leave(event):
        btn.configure(bg="#34495E" if dark_mode else "#D5D8DC")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    buttons.append(btn)

# Add buttons to the interface
for btn in button_config:
    if len(btn) == 4:  # Wide button (like "=")
        create_button(btn[0], evaluate, btn[1], btn[2], colspan=btn[3], wide=True)
    else:
        create_button(btn[0], lambda value=btn[0]: button_click(value) if value != 'C' else clear_entry(), btn[1], btn[2])

# Theme toggle button
theme_button = tk.Button(
    root,
    text="🌙",
    font=("Arial", 10, "bold"),
    bg="#34495E",
    fg="white",
    bd=0,
    command=toggle_theme,
    relief=tk.FLAT,
    width=2,
    height=1
)
theme_button.place(relx=0.9, rely=0.9, anchor="center")

# Apply initial theme
apply_theme()

# Run the application
root.mainloop()
