#Task 4: Display Budget Details Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

#Writing code for EncapsulationPersonalBudgetManagementTask4

#Copying code from EncapsulationPersonalBudgetManagementTask3

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

#Creating add expense method to take in expense amount with if statement to stop any negative expense amounts or expense amounts larger than budget
    def add_expense(self, amount):
        if 0 < amount <= self.get_allocated_budget():
            print(f"Original 'Food' budget: {self.__budget}")
            self.set_allocated_budget(self.get_allocated_budget() - amount)
            print(f"Subtracted Expense: {amount}")
            print(f"New Budget: {self.__budget}")
        else:
            print("Invalid amount or insuffecient funds.")

#Creating display method to display current food category and remaining budget amount after expenses as well as initializing attributes            
    def display_category_summary(self):
                print(f"\nDisplaying current budget category details\nBudget Category: {food_category.get_category_name()}\nAllocated budget: {food_category.get_allocated_budget()}")


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()