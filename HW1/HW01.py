"""
Georgia Institute of Technology - CS1301
HW01 - Functions & Expressions
"""

#########################################

"""
Function Name: tasteOfTech()
Parameters: N/A
Returns: None
"""
def tasteOfTech():
    name = input("What is your first name? ")
    tin_drum = float(input("How much did you spend at Tin Drum? "))
    waffle_house = float(input("How much did you spend at Waffle House? "))
    wild_wings = float(input("How much did you spend at Buffalo Wild Wings? "))
    total_cost = tin_drum + waffle_house + wild_wings
    doge = 14.57 * total_cost
    total_cost = round(total_cost, 2)
    doge = round(doge, 2)
    print("Congratulations {}! You spent ${} in total and earned {} DOGE.".format(name, total_cost, doge))

#tasteOfTech()

#########################################

"""
Function Name: shoppingMoney()
Parameters: N/A
Returns: None
"""
def shoppingMoney():
    income = float(input("How much is your monthly income? "))
    savings = float(0.6 * (income - 1020))
    savings = round(savings, 2)
    extra_money = float(0.4* (income - 1020))
    extra_money = round(extra_money, 2)
    print("You can save ${} and spend the remaining ${} on anything this month.".format(savings, extra_money))

#shoppingMoney()
    
#########################################

"""
Function Name: houseParty()
Parameters: N/A
Returns: None
"""
def houseParty():
    nuggets = int(input("How many chicken nuggets will each guest eat? "))
    rings = int(input("How many onion rings will each guest eat? "))
    donuts = int(input("How many donuts will each guest eat? "))
    cookies = int(input("How many cookies will each guest eat? "))
    guests = int(input("How many guests are you expecting at the party? "))
    
    nuggets = nuggets * guests
    rings = rings * guests
    donuts = donuts * guests
    cookies = cookies * guests
    
    print("You need to buy {} chicken nuggets, {} onion rings, {} donuts and {} cookies for {} guests.".format(nuggets, rings, donuts, cookies, guests))
   
#houseParty()
    
#########################################

"""
Function Name: spareTime()
Parameters: N/A
Returns: None
"""
def spareTime():
    total_credits = int(input("How many credits are you taking? "))
    spare_hours_week = 112 - (total_credits * 4)
    spare_hours = spare_hours_week // 7
    spare_mins = ((spare_hours_week / 7) -  spare_hours) * 60
    spare_mins = round(spare_mins, 1)
    print("You have {} hours and {} minutes per day to spare for other activities.".format(spare_hours, spare_mins))

#spareTime()

#########################################

"""
Function Name: ratsNight()
Parameters: N/A
Returns: None
"""
def ratsNight():
    games = int(input("How many slots would you like to book for video games? "))
    trivia = int(input("How many slots would you like to book for trivia time? "))
    arts = int(input("How many slots would you like to book for arts/crafts? "))
    total_time_mins = (games * 30) + (trivia * 10) + (arts * 45)
    hours = total_time_mins // 60
    mins = ((total_time_mins / 60) - hours) * 60
    mins = int(round(mins, 0))
    print("You will spend {} hours and {} minutes at Rats Night.".format(hours, mins))

#ratsNight()

















    
