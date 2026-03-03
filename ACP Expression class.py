# Creating the Expression class
class Expression:
    
    # Constructor to initialize num1, num2, num3
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    # Method to calculate addition
    def calculate_sum(self):
        result = self.num1 + self.num2 + self.num3
        print("The sum of", self.num1, ",", self.num2, "and", self.num3, "is:", result)

# Creating objects
exp1 = Expression(10, 20, 30)
exp2 = Expression(5, 15, 25)

# Calling method using objects
exp1.calculate_sum()
exp2.calculate_sum()