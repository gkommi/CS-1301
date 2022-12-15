"""
Georgia Institute of Technology - CS1301
HW07 -  File I/O
"""
#########################################
"""
Function Name: lazyMeal()
Parameters: maxPrepTime (int)
Returns: recipe (list)
"""
def lazyMeal(maxPrepTime):
    f = open("cookBook.txt", "r")
    f.readline()
    f.readline()
    file = f.read()
    f.close()
    recipeList = file.split()
    recipe = []
    for i in range(len(recipeList)):
        if str.isdigit(recipeList[i]) == False:
            continue
        else:
            if int(recipeList[i]) <= maxPrepTime:
                recipe.append(recipeList[i-1])
            else:
                continue
    recipe.sort()
    if len(recipe) == 0:
        return "Waffle House it is!"
    else:
        return recipe
""" 
print(lazyMeal(25))    
print(lazyMeal(5))
"""
#########################################
"""
Function Name: groupCountries()
Parameters: countries(list)
Returns: recipeDict (dict)
"""
def groupCountries(countries):
    f = open("cookBook.txt", "r")
    f.readline()
    f.readline()
    file = f.read()
    f.close()
    recipeList = file.split()
    #print(recipeList)
    recipeDict = {}
    for (name,country) in countries:
        list1 = []
        for i in range(len(recipeList)):
            if recipeList[i] == country:
                list1.append(recipeList[i-2])
                recipeDict[name] = list1
            else:
                continue
    if len(recipeDict) != len(countries):
        return "Throw the book or get new friends!"
    else:
        return recipeDict
"""  
countries = [("Marco", "Italy"), ("Isabelle", "India")]            
print(groupCountries(countries))
"""    
#########################################
"""
Function Name: favRecipes()
Parameters: recipeList (list)
Returns: None
"""
def favRecipes(recipeList):
    fav = open("favRecipes.txt", "w")    
    f = open("cookBook.txt", "r")
    f.readline()
    f.readline()
    file = f.read()
    f.close()
    #print(file)
    food1 = file.split()
    #print(food1)
    foodInfo = food1[:-2]
    foodInfo.append("Puerto Rico")
    #print(foodInfo)
    for p in range(len(recipeList)):
        if recipeList[p] not in foodInfo:
            result = True
        else:
            result = False
    
    if len(recipeList) == 0 or result:
            fav.write("No information found.")
    else:
        fav.write("Recipes\n\n")
        for p in range(len(recipeList)):
            for i in range(len(foodInfo)):
                if p + 1 == len(recipeList) and recipeList[p] == foodInfo[i]:
                    fav.write(foodInfo[i] + "\n")
                    fav.write(foodInfo[i+1] + "\n")
                    fav.write(foodInfo[i+2])
                else:
                    if recipeList[p] == foodInfo[i]:
                        fav.write(foodInfo[i] + "\n")
                        fav.write(foodInfo[i+1] + "\n")
                        fav.write(foodInfo[i+2] + "\n\n")                        
                    else:
                        continue
    fav.close()

#favRecipes(["Sushi", "Mofongo"])
#########################################
"""
Function Name: orderCandy()
Parameters: prices (dict), maxCost (float)
Returns: None
"""
def orderCandy(prices, maxCost):
    cd = open("candyOrder.txt", "w")
    friends = open("friends.txt", "r")
    file = friends.read()
    list1 = file.split()
    friends.close()
    print(list1)
    list2 = []
    for candy in prices:
        count = 0
        for i in range(len(list1)):
            if list1[i] == candy and prices[candy] <= maxCost:
                list2.append(candy)
                count += 1               
            else:
                continue
        if count != 0:
            cd.write(candy + ": " + str(count) + "\n")
    if len(list2) == 0:
        cd.write("Ask again.")
    #print(list2)       
    cd.close()
    'KitKats: 3\nM&Ms: 3\nReeses: 4\nStarburst: 1\n'
    'KitKats: 3\nM&Ms: 3\nReeses: 4'
"""
prices = {'KitKats': 2.0, 'M&Ms': 3.0, 'Hersheys': 3.5, 'Reeses': 1.5,
'Starburst': 2.0, 'Twix': 3.2, 'Jolly Ranchers': 2.6}
orderCandy(prices, 3.0)
"""
#########################################
"""
Function Name: moviePicker()
Parameters: potentialMovie (str)
Returns: isOption(bool)
"""
def moviePicker(potentialMovie):
    count = 0
    file1 = open("friends.txt")
    infile1 = open("movies.txt")
    friends = file1.read()
    friends1 = friends.split()
    movies = file2.readlines()
    for ind,w in enumerate(movies):
        w = w.strip()
        if w == potentialMovie:
            rating = movies[ind + 1]
            rating = int(rating)
    for i in friends1:
        try:
            i = int(i)
            if i >= rating:
                count += 1
        except:
            count += 0
    if count == 6:
        return True
    else:
        return False

    
"""
print(moviePicker("The Nightmare Before Christmas"))

"""
