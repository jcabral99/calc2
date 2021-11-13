"""This is the increment function"""
# first import the addition namespace
from Calc.addition import Addition

class Calculator:
    """This is the Calculator class"""
    history = []
    @staticmethod
    def history_count():
        return Calculator.history.count()
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
        return value_a - value_b
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiply two numbers and store the result"""
        return value_a * value_b