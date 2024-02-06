import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")

    if bmi <= 16:
        messagebox.showinfo("BMI Category", "Eat more")
    elif 16 <= bmi <= 25:
        messagebox.showinfo("BMI Category", "You're fine")
    elif bmi > 25:
        messagebox.showinfo("BMI Category", "Eat less")


frame = tk.Tk()
frame.title("BMI Calculator")
frame.geometry("250x150")

height_label = tk.Label(frame, text="Height:")
height_label.pack()
height_entry = tk.Entry(frame)
height_entry.pack()

weight_label = tk.Label(frame, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(frame)
weight_entry.pack()

calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

frame.mainloop()

