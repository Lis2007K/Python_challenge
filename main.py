from abc import ABC, abstractmethod

class Pearson(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @abstractmethod
    def calculate_bmi(self, weight, height, bmi):
        self.bmi = bmi
        bmi = weight/height**2
        pass

    @abstractmethod
    def get_bmi_category (self, bmi, age):
        pass

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, BMI: {self.calculate_bmi()}, Category: {self.get_bmi_category()}")

class Adult(Pearson):
    def calculate_bmi(self):
        return self.weight/self.height**2
    
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
        return self.weight/self.height**2*1.3
    
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