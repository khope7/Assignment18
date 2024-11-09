#Problem Statement: You are required to build a Personal Budget Management application.
#The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

#Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

#Writing code for EncapsulationPersonalBudgetManagementTask1

#Instantiating BudgetCategory class and initalizing private attributes for name and allocated budget
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__name = category_name
        self.__budget = allocated_budget

