#Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number)

#Writing code for EncapsulationPersonalBudgetManagementTask2

#Copying code from EncapsulationPersonalBudgetManagementTask1

#Instantiating BudgetCategory class and initalizing private attributes for name and allocated budget
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__name = category_name
        self.__budget = allocated_budget

#Initializing getters to return name and budget info
    def get_category_name(self):
        return self.__name
    
    def get_allocated_budget(self):
        return self.__budget

#Initializing setters to take in new name and amount
    def set_category_name(self, budget_name):
            self.__name = budget_name
        
    def set_allocated_budget(self, amount):
        self.__budget = amount

