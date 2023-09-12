import Decorator_Design_Pattern as dd


myCoffee = dd.Concrete_Coffee()
print(f"Ingredients: {myCoffee.get_ingredients()}; Cost: {str(myCoffee.get_cost())}; "
      f"sales tax = {str(myCoffee.get_tax())}")

myCoffee = dd.Milk(myCoffee)
print(f"Ingredients: {myCoffee.get_ingredients()}; Cost: {str(myCoffee.get_cost())}; "
      f"sales tax = {str(myCoffee.get_tax())}")

myCoffee = dd.Vanilla(myCoffee)
print(f"Ingredients: {myCoffee.get_ingredients()}; Cost: {str(myCoffee.get_cost())}; "
      f"sales tax = {str(myCoffee.get_tax())}")

myCoffee = dd.Sugar(myCoffee)
print(f"Ingredients: {myCoffee.get_ingredients()}; Cost: {str(myCoffee.get_cost())}; "
      f"sales tax = {str(myCoffee.get_tax())}")
