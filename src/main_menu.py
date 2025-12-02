import os
from operations.addition import addition

class Menu:
    def __init__(self) -> None:
        self.user_selected_option: bool = False
        self.first_number: float
        self.second_number: float
        self.first_user_input: str
        self.second_user_input: str
        
    def interface(self):
        os.system('cls' if os.name == 'nt' else 'clear')
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
                result = addition(3,5)
                print(result)
                input()
                self.user_selected_option = False
            case 0:
                self.user_selected_option = True
            case _:
                self.user_selected_option = False
            
    def user_interaction(self):
        while True:
            user_input = input()
            if self.validate_input(user_input):
                return int(user_input)
            else:
                continue    
        
    def validate_input(self, user_input: str):
        if user_input.isdecimal():
            return True
        else:
            print("Erreur: Seuls les chiffres sont acceptés")
            return False
    
    def display_menu(self):
        while self.user_selected_option == False:
            self.interface()
            self.navigation()

calculator = Menu()
calculator.display_menu()