import tkinter as tk

def submit_character():
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

# Create the main window
root = tk.Tk()
root.title("D&D 3.5 Character Creator")

# Create and place labels and entry fields for character attributes
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Race:").grid(row=1, column=0)
race_entry = tk.Entry(root)
race_entry.grid(row=1, column=1)

tk.Label(root, text="Class:").grid(row=2, column=0)
class_entry = tk.Entry(root)
class_entry.grid(row=2, column=1)

tk.Label(root, text="Strength:").grid(row=3, column=0)
strength_entry = tk.Entry(root)
strength_entry.grid(row=3, column=1)

tk.Label(root, text="Dexterity:").grid(row=4, column=0)
dexterity_entry = tk.Entry(root)
dexterity_entry.grid(row=4, column=1)

tk.Label(root, text="Constitution:").grid(row=5, column=0)
constitution_entry = tk.Entry(root)
constitution_entry.grid(row=5, column=1)

tk.Label(root, text="Intelligence:").grid(row=6, column=0)
intelligence_entry = tk.Entry(root)
intelligence_entry.grid(row=6, column=1)

tk.Label(root, text="Wisdom:").grid(row=7, column=0)
wisdom_entry = tk.Entry(root)
wisdom_entry.grid(row=7, column=1)

tk.Label(root, text="Charisma:").grid(row=8, column=0)
charisma_entry = tk.Entry(root)
charisma_entry.grid(row=8, column=1)

# Create a submit button to gather character information
submit_button = tk.Button(root, text="Submit", command=submit_character)
submit_button.grid(row=9, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
