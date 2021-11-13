"""This is the increment function"""
# first import the addition namespace
from Calc.addition import Addition
from Calc.subtraction import Subtraction
from Calc.multiplication import Multiplication
from Calc.division import Division

class Calculator:
    """This is the Calculator class"""
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].getresult()
    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        # -1 gets the last item added to the list automatically and you can expect it to have the get result method
        return Calculator.history[-1].getresult()
    @staticmethod
    def add_number(value_a, value_b):
        """adds number to result"""
        #create an addition object using the factory we created on the calculation class
        addition = Addition.create(value_a,value_b)
        # addition = addition(value_a, value_b) <-this is not good but will work. It will be repeated too much
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def subtract_number(value_a, value_b):
        """"subtract number from result"""
        # create an subtract object using the factory we created on the calculation class
        subtraction = Subtraction.create(value_a, value_b)
         # addition = addition(value_a, value_b) <-this is not good but will work. It will be repeated too much
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiply two numbers and store the result"""
        multiplication = Multiplication.create(value_a,value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def divide_numbers(value_a,value_b):
        """divide two numbers and store the result"""
        division = Division.create(value_a,value_b)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_result_of_last_calculation_added_to_history()
