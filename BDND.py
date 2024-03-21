import tkinter as tk
from tkinter import filedialog

def submit_character():
    try:
        # Gather character attributes
        character = {
            "Name": name_entry.get(),
            "Race": race_entry.get(),
            "Class": class_entry.get(),
            "Strength": int(strength_entry.get()),
            "Dexterity": int(dexterity_entry.get()),
            "Constitution": int(constitution_entry.get()),
            "Intelligence": int(intelligence_entry.get()),
            "Wisdom": int(wisdom_entry.get()),
            "Charisma": int(charisma_entry.get())
        }
        print(character)
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter numeric values for ability scores.")

def save_character():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write("Character Sheet\n\n")
            file.write(f"Name: {name_entry.get()}\n")
            file.write(f"Race: {race_entry.get()}\n")
            file.write(f"Class: {class_entry.get()}\n")
            file.write(f"Strength: {strength_entry.get()}\n")
            file.write(f"Dexterity: {dexterity_entry.get()}\n")
            file.write(f"Constitution: {constitution_entry.get()}\n")
            file.write(f"Intelligence: {intelligence_entry.get()}\n")
            file.write(f"Wisdom: {wisdom_entry.get()}\n")
            file.write(f"Charisma: {charisma_entry.get()}\n")
        print("Character saved successfully.")

def load_character():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            lines = file.readlines()
            # Extract character attributes from the file
            character = {}
            for line in lines:
                key, value = line.strip().split(": ")
                character[key] = value
            # Display character attributes in the entry fields
            name_entry.delete(0, tk.END)
            name_entry.insert(0, character["Name"])
            race_entry.delete(0, tk.END)
            race_entry.insert(0, character["Race"])
            class_entry.delete(0, tk.END)
            class_entry.insert(0, character["Class"])
            strength_entry.delete(0, tk.END)
            strength_entry.insert(0, character["Strength"])
            dexterity_entry.delete(0, tk.END)
            dexterity_entry.insert(0, character["Dexterity"])
            constitution_entry.delete(0, tk.END)
            constitution_entry.insert(0, character["Constitution"])
            intelligence_entry.delete(0, tk.END)
            intelligence_entry.insert(0, character["Intelligence"])
            wisdom_entry.delete(0, tk.END)
            wisdom_entry.insert(0, character["Wisdom"])
            charisma_entry.delete(0, tk.END)
            charisma_entry.insert(0, character["Charisma"])
        print("Character loaded successfully.")

# Create the main window
root = tk.Tk()
root.title("D&D 3.5 Character Creator")
root.geometry("400x300")  # Increase window size

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Character", command=save_character)
file_menu.add_command(label="Load Character", command=load_character)

# Create and place labels and entry fields for character attributes
# (Note: The rest of the GUI components remain unchanged)

# Start the Tkinter event loop
root.mainloop()
