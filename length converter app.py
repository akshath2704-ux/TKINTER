import tkinter as tk

class LengthConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Length Converter")


        tk.Label(self.window, text="Length (inches):").grid(row=0, column=0)

        self.length_inches = tk.Entry(self.window)
        self.length_inches.grid(row=0, column=1)

        tk.Button(self.window, text="Convert to Centimeters", command=self.convert_length).grid(row=1, column=0, columnspan=2)

        self.result = tk.Label(self.window, text="")
        self.result.grid(row=2, column=0, columnspan=2)

    def convert_length(self):
        try:
            length_inches = float(self.length_inches.get())
            length_cm = length_inches * 2.54
            self.result['text'] = f"{length_inches} inches is equal to {length_cm} centimeters."
        except ValueError:
            self.result['text'] = "Invalid input. Please enter a valid number."

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = LengthConverter()
    app.run()
