import customtkinter as ctk
import random
import string


# Function to generate the password
def generate_password():
    try:
        length = int(slider_length.get())

        # Get character sets based on checkboxes
        character_pool = ""
        if var_uppercase.get():
            character_pool += string.ascii_uppercase
        if var_lowercase.get():
            character_pool += string.ascii_lowercase
        if var_numbers.get():
            character_pool += string.digits
        if var_symbols.get():
            character_pool += string.punctuation

        if not character_pool:
            label_status.configure(text="Error: Select at least one character type!", text_color="red")
            return

        # Generate the password
        password = ''.join(random.choice(character_pool) for _ in range(length))
        entry_password.delete(0, ctk.END)
        entry_password.insert(0, password)
        label_status.configure(text="Password generated successfully!", text_color="green" ,font =("Roboto Mono", 14, "bold"))
    except Exception as e:
        label_status.configure(text=f"Error: {e}", text_color="red")


# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        label_status.configure(text="Password copied to clipboard!", text_color="green")
    else:
        label_status.configure(text="Error: No password to copy!", text_color="red")


def update_length_label(value):
    label_length_value.configure(text=f"{int(float(value))}")


# Main window
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Password Generator")
root.geometry("500x480")
root.resizable(False, False)

label_title = ctk.CTkLabel(root, text="Password Generator", font=("Poppins", 20, "bold"))
label_title.pack(pady=10)

# Password Length
frame_length = ctk.CTkFrame(root)
frame_length.pack(pady=10, padx=20, fill="x")

label_length = ctk.CTkLabel(frame_length, text="Password Length:", font=("Arial", 14))
label_length.pack(side="left", padx=10, pady=5)

slider_length = ctk.CTkSlider(frame_length, from_=6, to=64, number_of_steps=58, width=200, command=update_length_label)
slider_length.pack(side="left", padx=10)
slider_length.set(12)

label_length_value = ctk.CTkLabel(frame_length, text="12", font=("Arial", 14, "bold"))
label_length_value.pack(side="left", padx=10)

# Character Options
frame_options = ctk.CTkFrame(root)
frame_options.pack(pady=10, padx=20, fill="x")

var_uppercase = ctk.BooleanVar(value=True)
checkbox_uppercase = ctk.CTkCheckBox(frame_options, text="Include Uppercase Letters", variable=var_uppercase)
checkbox_uppercase.pack(anchor="w", pady=5, padx=10)

var_lowercase = ctk.BooleanVar(value=True)
checkbox_lowercase = ctk.CTkCheckBox(frame_options, text="Include Lowercase Letters", variable=var_lowercase)
checkbox_lowercase.pack(anchor="w", pady=5, padx=10)

var_numbers = ctk.BooleanVar(value=True)
checkbox_numbers = ctk.CTkCheckBox(frame_options, text="Include Numbers", variable=var_numbers)
checkbox_numbers.pack(anchor="w", pady=5, padx=10)

var_symbols = ctk.BooleanVar(value=True)
checkbox_symbols = ctk.CTkCheckBox(frame_options, text="Include Symbols", variable=var_symbols)
checkbox_symbols.pack(anchor="w", pady=5, padx=10)

# Generate Button
button_generate = ctk.CTkButton(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

# Password Display
entry_password = ctk.CTkEntry(root, width=400, font=("Arial", 14), justify="center")
entry_password.pack(pady=10)
button_copy = ctk.CTkButton(root, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=10)

# Status Label
label_status = ctk.CTkLabel(root, text="", font=("Arial", 12))
label_status.pack(pady=10)
root.mainloop()