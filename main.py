import tkinter as tk
from tkinter import ttk

#Window
window = tk.Tk()
window.title('Tkinter Variables')

#tkinter variable
string_var = tk.StringVar(value='test')

#Widgets
label = ttk.Label(master=window,text='Label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack()

#Run
window.mainloop()

