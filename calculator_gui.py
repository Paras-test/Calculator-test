import tkinter as tk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.calc = Calculator()
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        self.result = tk.Label(self.window, text="")
        self.result.pack()
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()
        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add)
        self.add_button.pack(side=tk.LEFT)
        self.subtract_button = tk.Button(self.button_frame, text="Subtract", command=self.subtract)
        self.subtract_button.pack(side=tk.LEFT)
        self.multiply_button = tk.Button(self.button_frame, text="Multiply", command=self.multiply)
        self.multiply_button.pack(side=tk.LEFT)
        self.divide_button = tk.Button(self.button_frame, text="Divide", command=self.divide)
        self.divide_button.pack(side=tk.LEFT)
    def add(self):
        try:
            num1, num2 = map(float, self.entry.get().split(','))
            result = self.calc.add(num1, num2)
            self.result.config(text=f"Result: {result}")
        except Exception as e:
            self.result.config(text=f"Error: {e}")
    def subtract(self):
        try:
            num1, num2 = map(float, self.entry.get().split(','))
            result = self.calc.subtract(num1, num2)
            self.result.config(text=f"Result: {result}")
        except Exception as e:
            self.result.config(text=f"Error: {e}")
    def multiply(self):
        try:
            num1, num2 = map(float, self.entry.get().split(','))
            result = self.calc.multiply(num1, num2)
            self.result.config(text=f"Result: {result}")
        except Exception as e:
            self.result.config(text=f"Error: {e}")
    def divide(self):
        try:
            num1, num2 = map(float, self.entry.get().split(','))
            result = self.calc.divide(num1, num2)
            self.result.config(text=f"Result: {result}")
        except Exception as e:
            self.result.config(text=f"Error: {e}")
    def run(self):
        self.window.mainloop()

gui = CalculatorGUI()
gui.run()