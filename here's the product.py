import tkinter as tk

class ProductCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Product Calculator")
        tk.Label(self.window, text="Number 1:").grid(row=0, column=0)
        tk.Label(self.window, text="Number 2:").grid(row=1, column=0)

        self.num1 = tk.Entry(self.window)
        self.num2 = tk.Entry(self.window)

        self.num1.grid(row=0, column=1)
        self.num2.grid(row=1, column=1)

        tk.Button(self.window, text="Calculate Product", command=self.calculate_product).grid(row=2, column=0, columnspan=2)

        self.result = tk.Label(self.window, text="")
        self.result.grid(row=3, column=0, columnspan=2)

    def calculate_product(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            product = num1 * num2
            self.result['text'] = f"The product is: {product}"
        except ValueError:
            self.result['text'] = "Invalid input. Please enter valid numbers."

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ProductCalculator()
    app.run()


