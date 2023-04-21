import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

# Create a custom style for the label
style = ttk.Style()

# Configure a labelframe with a border width and color
style.configure('RoundedLabelFrame.TLabelframe', borderwidth=10, bordercolor='blue')

# Configure a label with padding to create the rounded corners
style.configure('RoundedLabel.TLabel', padding=(30, 30, 30, 30), relief='raised', background='white')

# Create a labelframe and label using the custom style
label_frame = ttk.Frame(root, style='RoundedLabelFrame.TLabelframe')
label_frame.pack(padx=20, pady=20)

label = ttk.Label(label_frame, text='Hello, world!', style='RoundedLabel.TLabel')
label.pack(padx=10, pady=10)

root.mainloop()
