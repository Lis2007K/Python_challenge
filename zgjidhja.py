from abc import ABC, abstractmethod

class Pearson(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight =weight
        self._height = height

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        if value < 0 :
            raise ValueError("Weight smumet me qen 0 ose ma pak")
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value < 0 :
            raise ValueError("Height smumet me qen 0 ose ma pak")
        
    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(
            f"Name:{self.name}, Age:{self.age}, Weight:{self._weight}, Height:{self.height}"
            f"{self.calculate_bmi(), self.get_bmi_category()}"
        )

class Adult(Pearson):
    def calculate_bmi(self):
        return self.weight/(self.height**2)
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5 :
            return "Underwight"
        elif 18.5 <= bmi < 24.9:
            return "Normal Weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        elif bmi >= 29.9:
            return "Obese"
        
class Child(Pearson):
    def calculate_bmi(self):
        return (self.weight/(self.height**2))*1.3
    
    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14 :
            return "Underwight"
        elif 14 <= bmi < 18:
            return "Normal Weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        elif bmi >= 24:
            return "Obese"
        
class BMIApp:
    def __init__(self):
        self.people = []

    def add_pearson(self, pearson):
        self.people.append(pearson)

    def collect_user_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        height = float(input("Enter height"))
        weight = float(input("Enter weight:"))

        if age >= 18:
            pearson = Adult(name, age, weight, height)