import os
from operations.addition import addition
from operations.subtraction import subtraction

class Menu:
    def __init__(self) -> None:
        self.user_selected_option: bool = False
        self.first_number: float
        self.second_number: float
        self.first_user_input: str
        self.second_user_input: str
        
    def interface(self):
        print("== Calculatrice Python ==")
        print("1 - Addition")
        print("2 - Substraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Puissance")
        print("6 - Racine carée")
        print("7 - Historique")
        print("0 - Quitter")
            
    def navigation(self):
        inputed_number: int = self.user_interaction()
        match inputed_number:
            case 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.calculate()
                result = addition(self.first_number, self.second_number)
                print(f"{self.first_number} + {self.second_number} = {result}")
                input("Appuyez sur une touche...")
                os.system('cls' if os.name == 'nt' else 'clear')
                self.user_selected_option = False
            case 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.calculate()
                result = subtraction(self.first_number, self.second_number)
                print(f"{self.first_number} - {self.second_number} = {result}")
                input("Appuyez sur une touche...")
                os.system('cls' if os.name == 'nt' else 'clear')
                self.user_selected_option = False
            case 0:
                self.user_selected_option = True
            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.user_selected_option = False
            
    def user_interaction(self):
        while True:
            user_input = input()
            if self.validate_input(user_input):
                return int(user_input)
            else:
                input()
                os.system('cls' if os.name == 'nt' else 'clear')
                continue    
        
    def validate_input(self, user_input: str):
        if user_input.isdecimal():
            return True
        else:
            print("Erreur: Seuls les chiffres sont acceptés")
            return False
    
    def calculate(self):
        while True:
            self.ask_user_inputs()
            if self.validate_inputs(self.first_user_input, self.second_user_input):
                self.first_number = float(self.first_user_input)
                self.second_number = float(self.second_user_input)
                break
            else:
                print("Erreur: Veuillez entrer des nombres valides")
                continue
        
    def ask_user_inputs(self):
        self.first_user_input = input("Insérez un premier nombre: ")
        self.second_user_input = input("Insérez un deuxième nombre: ")
    
    def validate_inputs(self, input_1: str, input_2: str):
        try:
            float(input_1)
            try:
                float(input_2)
                return True
            except ValueError:
                return False
        except ValueError:
            return False
    
    def display_menu(self):
        while self.user_selected_option == False:
            self.interface()
            self.navigation()

calculator = Menu()
calculator.display_menu()