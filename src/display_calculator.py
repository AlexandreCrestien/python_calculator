from calculator import Calculator

class DisplayCalculator:
    def __init__(self):
        self.calc = Calculator()

    def display_addition(self, a, b):
        result = self.calc.addition(a, b)
        print(f"le resultat de l'addition de {a} et {b} est: {result}")