class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        # TODO: Implement multiplication
        pass
        
    def divide(self, a, b):
        # TODO: Implement division
        pass

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Partial Calculator!")
    print("10 + 5 =", calc.add(10, 5))
