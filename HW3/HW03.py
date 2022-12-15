"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: product()
Parameters: nums(str)
Returns: product(int)
"""
def product(nums):
    length = len(nums)
    product = 1
    i = 0
    while i < length:
        product = product * int(nums[i])
        i += 1
    return product
        
#print(product("14123"))
#print(product("586930"))

    
#########################################
"""
Function Name: recipeCount()
Parameters: recipe(str)
Returns: totalTeaspoons(int)
"""
def recipeCount(recipe):
    totalTeaspoons = 0
    if len(recipe) == 0:
        totalTeaspoons = 0
    else:
        for num in recipe:
            if (num.isdigit()):
                totalTeaspoons = totalTeaspoons + int(num)
            continue     
    return totalTeaspoons

#print(recipeCount("3 teaspoon of broccoli, 7 teaspoons of lettuce"))
    
#########################################
"""
Function Name: instagraminator()
Parameters: usernames(str)
Returns: decodedUsernames(str)
"""
def instagraminator(usernames):
    for char in usernames:
        if "@" in usernames:
            usernames = usernames.replace("@", "")
        if "_" in usernames:
            usernames = usernames.replace("_", "")
        if "$" in usernames:
            usernames = usernames.replace("$", "")
    return usernames

#print(instagraminator("@josh_The_TA, @$Queen$Parul$, @Party_$_Paige"))
    
#########################################
"""
Function Name: studentLoans()
Parameters: loanAmount(int)
Returns: forgivenessCount(int)
"""
def studentLoans(loanAmount):
    i = 0
    while loanAmount > 0:
        loanAmount = loanAmount - 10000
        i += 1
    return i

#print(studentLoans(200001))
    
#########################################
"""
Function Name: playoffs()
Parameters: team1name (str), team2name (str), scoreCount (str) 
Returns: winningTeam (str) 
"""
def playoffs(team1name, team2name, scoreCount):
    num1 = 0
    num2 = 0
    for score in scoreCount:
        if score == "1":
            num1 += 1
        if score == "2":
            num2 += 1
    if num1 > num2:
        winningTeam = "{} has won the game!".format(team1name)
    elif num1 < num2:
        winningTeam = "{} has won the game!".format(team2name)
    else:
        winningTeam = "It was a tie :("
    return winningTeam

#print(playoffs("Parul", "Josh", "1111112221"))
    
            









    
    
    
