import tkinter as tk
from datetime import date

class AgeCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Age Calculator")

        # Create input fields
        tk.Label(self.window, text="Date (DD):").grid(row=0, column=0)
        tk.Label(self.window, text="Month (MM):").grid(row=1, column=0)
        tk.Label(self.window, text="Year (YYYY):").grid(row=2, column=0)

        self.date = tk.Entry(self.window)
        self.month = tk.Entry(self.window)
        self.year = tk.Entry(self.window)

        self.date.grid(row=0, column=1)
        self.month.grid(row=1, column=1)
        self.year.grid(row=2, column=1)

        tk.Button(self.window, text="Calculate Age", command=self.calculate_age).grid(row=3, column=0, columnspan=2)

        self.result = tk.Label(self.window, text="")
        self.result.grid(row=4, column=0, columnspan=2)

    def calculate_age(self):
        try:
            day = int(self.date.get())
            month = int(self.month.get())
            year = int(self.year.get())

            today = date.today()
            age = today.year - year - ((today.month, today.day) < (month, day))
            self.result['text'] = f"You are {age} years old."
        except ValueError:
            self.result['text'] = "Invalid input. Please enter valid numbers."

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = AgeCalculator()
    app.run()
