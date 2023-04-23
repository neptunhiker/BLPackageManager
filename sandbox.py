import tkinter as tk
import tkinter.ttk as ttk

# create a ttkbootstrap style
style = ttk.Style()

# configure the style to use a yellow border
style.configure('Yellow.TFrame', bordercolor='yellow')

# create a tkinter window
root = tk.Tk()

# create a frame with the Yellow.TFrame style
frame = ttk.Frame(root, style='Yellow.TFrame')

# add widgets to the frame
label = ttk.Label(frame, text='This is a yellow frame')
label.pack(padx=10, pady=10)

# pack the frame in the window
frame.pack()

# start the tkinter event loop
root.mainloop()
