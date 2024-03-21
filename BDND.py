import tkinter as tk

# Event handler function
def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Brandon's DnD Generator")

# Create a button widget
button = tk.Button(root, text="Click Me!", command=on_button_click)

# Add the button to the window
button.pack()

# Create a label widget
label = tk.Label(root, text="")

# Add the label to the window
label.pack()

# Run the Tkinter event loop
root.mainloop()
