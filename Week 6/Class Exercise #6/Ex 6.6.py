import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry("300x200")
win.title("Number Calculator")

# create labels and entry widgets for the numbers
lblNum1 = tk.Label(win, text="Enter Number 1:")
lblNum1.grid(column=0, row=0)
num1 = tk.StringVar()
txtNum1 = tk.Entry(win, width=12, textvariable=num1)
txtNum1.grid(column=1, row=0)

lblNum2 = tk.Label(win, text="Enter Number 2:")
lblNum2.grid(column=0, row=1)
num2 = tk.StringVar()
txtNum2 = tk.Entry(win, width=12, textvariable=num2)
txtNum2.grid(column=1, row=1)

lblNum3 = tk.Label(win, text="Enter Number 3:")
lblNum3.grid(column=0, row=2)
num3 = tk.StringVar()
txtNum3 = tk.Entry(win, width=12, textvariable=num3)
txtNum3.grid(column=1, row=2)

# create labels to display the sum and average
lblSum = tk.Label(win, text="Sum:")
lblSum.grid(column=0, row=3)
sum_val = tk.StringVar()
lblSumResult = tk.Label(win, textvariable=sum_val)
lblSumResult.grid(column=1, row=3)

lblAvg = tk.Label(win, text="Average:")
lblAvg.grid(column=0, row=4)
avg_val = tk.StringVar()
lblAvgResult = tk.Label(win, textvariable=avg_val)
lblAvgResult.grid(column=1, row=4)

# function to calculate sum and average of numbers and update labels
def compute():
    n1 = float(num1.get())
    n2 = float(num2.get())
    n3 = float(num3.get())
    sum_nums = n1 + n2 + n3
    avg_nums = sum_nums / 3
    sum_val.set(str(sum_nums))
    avg_val.set(str(avg_nums))

# function to write the results to a text file
def write():
    sum_nums = float(sum_val.get())
    avg_nums = float(avg_val.get())
    with open("Number Calculator.txt", "a") as f:
        f.write("Sum: " + str(sum_nums) + "\n")
        f.write("Average: " + str(avg_nums) + "\n")
    messagebox.showinfo("Information", "Data recorded successfully.")

# create buttons to compute and transfer the results
btnCompute = tk.Button(win, text="Compute", command=compute)
btnCompute.grid(column=0, row=5)

btnTransfer = tk.Button(win, text="Transfer", command=write)
btnTransfer.grid(column=1, row=5)

win.mainloop()
