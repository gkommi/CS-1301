"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""
#########################################
class People:
  def __init__(self, param1, param2, param3, param4=False):
    self.name = param1
    self.age = param2
    self.isAsleep = param3
    self.canCook = param4
    self.friends = []
  def __repr__(self): #provided
    return f"People({self.name}, {self.age}, {self.isAsleep}, {self.canCook}, {len(self.friends)})"
  def __eq__(self, other): #provided
    return self.name==other.name and self.age==other.age and self.isAsleep==other.isAsleep and self.canCook==other.canCook and self.friends==other.friends
  def wakeUp(self):
    if self.isAsleep == True:
      self.isAsleep = False
    else:
      return "{} is already awake.".format(self.name)
    
  def invite(self, other):
    self.friends.append(other)
    
  def __str__(self):
    if self.canCook == True:
      return "My name is {} and I can cook.".format(self.name)
    else:
      return "My name is {} and I can't cook.".format(self.name)
  def __lt__(self, other):
    return self.age < other.age

#########################################
class Food:
  def __init__(self, param1, param2, param3):
    self.name = param1
    self.ingredients = param2
    self.prepTime = param3
  def __repr__(self): #provided
    return f"Food({self.name}, {len(self.ingredients)}, {self.prepTime})"
  def __str__(self):
    return "{} takes {} to make.".format(self.name, self.prepTime)
  
#########################################
class Activities:
  def __init__(self, param1={}):
    self.ingredientsDict = param1
  def __repr__(self): #provided
    return f"Activities({len(self.ingredientsDict)})"
  def cook(self,food):
    for name,quantity in food.ingredients:
      if quantity > self.ingredientsDict[name]:
        return "We did not have enough ingredients to make {}.".format(food.name)
    for name,quantity in food.ingredients:
      self.ingredientsDict[name] -= quantity
    return "We made {}!".format(food.name)
  
  def kidsTable(self,guests):
    list1 = []
    list2 = []
    for person in guests:
      tup1 = (person.age, person.name)
      list1.append(tup1)
    list1.sort()
    list1 = list1[:4]
    for age,name in list1:
      list2.append(name)
    return list2

  def buyIngredients(self, ingredientName, ingredientAmount):
    if ingredientName not in self.ingredientsDict:
      self.ingredientsDict[ingredientName] = ingredientAmount
    else:
      self.ingredientsDict[ingredientName] += ingredientAmount
    
    
"""
activity = Activities({"flour": 6, "eggs": 12, "milk": 2, "turkey": 1, "apples": 3, "butter": 2})
food = Food("Apple Pie", [("flour",4),("eggs",6),("milk",.3),
                          ("butter",.2),("apples",2)], 46)
print(activity.cook(food))
"""












































