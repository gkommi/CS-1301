"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: availableDate()
Parameters: date(int), isWeekend(bool)
Returns: availability(str)
"""
def availableDate(date, isWeekend):
    if isWeekend == True or date % 2 == 0:
        availability = "Available on {}!".format(date)
    else:
        availability = "Not available :("
    return availability

#date1 = availableDate(29, False)
#print(date1)
        

#########################################

"""
Function Name: buyGame()
Parameters: gameTitle(str), budget(float), cost(float), positiveRating(float)
Returns: None(NoneType)
"""
def buyGame(gameTitle, budget, cost, positiveRating):
    if cost > budget:
        print("{} is over ${}!".format(gameTitle, budget))
    if cost <= budget and positiveRating >= 0.7:
        print("Sasuke will buy {}!".format(gameTitle))
    if cost <= budget and positiveRating < 0.7:
        print("Let's find another game.")

#buyGame("Splatoon 3", 80.0, 59.99, .87)
#buyGame("Elden Ring", 9000.0, 9001.0, .9)

"""
game1 = buyGame("Splatoon 3", 80.0, 59.99, .87)
print(game1)
game2 = buyGame("Elden Ring", 9000.0, 9001.0, .9)
print(game2)
"""
#########################################

"""
Function Name: foodTime()
Parameters: restaurant(str), time(int)
Returns: howLong(float or int)
"""
def foodTime(restaurant, time):
    if restaurant == "Cafe Leblanc":
        howLong = time - 15 - 2 * (620 / 80)
    if restaurant == "The Roost":
        howLong = time - 20 - 2 * (700 / 80)
    if restaurant == "Lumpy Pumpkin":
        howLong = time - 22 - 2 * (850 / 80)
    if restaurant == "The Milk Bar":
        howLong = time - 13 - 2 * (1200 / 80)
    if howLong >= 0:
        return howLong
    else:
        return -1   
"""
food1 = foodTime("Cafe Leblanc", 50)
print(food1)
food2 = foodTime("Lumpy Pumpkin", 40)
print(food2)
"""
#########################################

"""
Function Name: restaurantReservation()
Parameters: total(int), toSave(int), average(int)
Returns: canReserve(bool)
"""
def restaurantReservation(total, toSave, average):
    moneyLeft = total -  toSave
    if (moneyLeft / (average * 2)) > 1:
        return True
    else:
        return False
    
"""
r1 = restaurantReservation(400, 250, 50)
print(r1)
r2 = restaurantReservation(200, 180, 15)
print(r2)
"""

#########################################

"""
Function Name: halloweenHeist()
Parameters: num1(int), num2(int), name(str)
Returns: message(str)
"""
def halloweenHeist(num1, num2, name):
    diff = num1 - num2
    if diff > 0:
        message = "{} has the package.".format(name)
    elif diff < 0:
        message = "{} does not have the package.".format(name)
    elif diff == 0:
        message = "{} has taken over.".format(name)
    return message

"""
h1 = halloweenHeist(20, 16, 'Jake')
print(h1)
h2 = halloweenHeist(13, 25, 'Holt')
print(h2)
"""





    
