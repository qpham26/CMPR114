import tkinter as tk

# function to read the file and display the data
def read_file():
    try:
        with open('numbers.txt', 'r') as file:
            data = file.read()
            display_label.config(text=data)
    except FileNotFoundError:
        display_label.config(text='File not found')

# function to calculate and display the total
def calculate_total():
    try:
        with open('numbers.txt', 'r') as file:
            numbers = [int(num) for num in file]
            total = sum(numbers)
            display_label.config(text=f'Total: {total}')
    except FileNotFoundError:
        display_label.config(text='File not found')

# create the GUI
root = tk.Tk()
root.geometry('400x200')
root.title('File Reader')

# create the widgets
title_label = tk.Label(root, text='File Reader', font=('Helvetica', 16))
read_button = tk.Button(root, text='Read File', command=read_file)
calculate_button = tk.Button(root, text='Calculate Total', command=calculate_total)
display_label = tk.Label(root, text='')

# add the widgets to the window
title_label.pack(pady=10)
read_button.pack()
calculate_button.pack(pady=10)
display_label.pack()

# run the main loop
root.mainloop()
