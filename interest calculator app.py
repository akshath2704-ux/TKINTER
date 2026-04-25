import tkinter as tk

class InterestCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interest Calculator")

        tk.Label(self.window, text="Principal Amount:").grid(row=0, column=0)
        tk.Label(self.window, text="Interest Rate (%):").grid(row=1, column=0)
        tk.Label(self.window, text="Time (years):").grid(row=2, column=0)

        self.principal = tk.Entry(self.window)
        self.interest_rate = tk.Entry(self.window)
        self.time = tk.Entry(self.window)

        self.principal.grid(row=0, column=1)
        self.interest_rate.grid(row=1, column=1)
        self.time.grid(row=2, column=1)

        tk.Button(self.window, text="Calculate Interest", command=self.calculate_interest).grid(row=3, column=0, columnspan=2)

        self.result = tk.Label(self.window, text="")
        self.result.grid(row=4, column=0, columnspan=2)

    def calculate_interest(self):
        try:
            principal = float(self.principal.get())
            interest_rate = float(self.interest_rate.get()) / 100
            time = float(self.time.get())

            simple_interest = principal * interest_rate * time
            compound_interest = principal * ((1 + interest_rate))