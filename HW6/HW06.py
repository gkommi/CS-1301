"""
Georgia Institute of Technology - CS1301
HW06 -  Dictionaries and Try/Except
"""
#########################################
"""
Function Name: dinnerTimer()
Parameters: meal (str), diningHalls (dict)
Returns: optionsList (list)
"""
def dinnerTime(meal, diningHalls):
    optionsList = []
    for key in diningHalls:
        for items in diningHalls[key]:
            if meal == items:
                optionsList.append(key)
    if len(optionsList) == 0:
        return "Eat at home!"
    else:
        return optionsList
"""
diningHalls = {
    "Willage" : ("Mystery Meat", "Taco Salad", "Quinoa Casserole"),
    "Brittain" : ("Veggie Burger", "Cheeto Sushi", "Cereal"),
    "Nave" : ("Cereal",)
    }
meal = "Cereal"
print(dinnerTime(meal, diningHalls))
"""
#########################################
"""
Function Name: rateActor()
Parameters: skillScore (list), fanScore (List)
Returns: totalScores (dict)
"""
def rateActor(skillScore, fanScore):
    totalScores = {}
    for i in range(len(skillScore)):
        score = 0
        try:
            score += skillScore[i][1] + fanScore[i][1]
        except:
            typeSkill = type(skillScore[i][1])
            typeFan = type(fanScore[i][1])
            if (typeSkill == int or typeSkill == float) and (typeFan != int or typeFan != float):
                score += skillScore[i][1] + 3
            elif (typeSkill != int or typeSkill != float) and (typeFan == int or typeFan == float):
                score += fanScore[i][1] + 3
            else:
                score = 6
        totalScores[skillScore[i][0]] = score
    return totalScores

"""
skillScore = [("HS", 1), ("FP", 5.0), ("CP", 4), ("OW", "%%%%")]
fanScore = [("HS", 5), ("FP", 5), ("CP", None), ("OW", 2)]
print(rateActor(skillScore, fanScore))
"""
"""
skillScore = [("HS", 3), ("FP", [5]), ("CP", 3), ("OW", {2:2})]
fanScore = [("HS", 4), ("FP", 5), ("CP", (2,)), ("OW", 2)]
print(rateActor(skillScore, fanScore))
"""
#########################################
"""
Function Name: theRealDeal()
Parameters: stockDict (dict), goodStock (str)
Returns: richList (list)
"""
def theRealDeal(stockDict, goodStock):
    one = []
    if goodStock in stockDict.keys():
        earnings1 = stockDict[goodStock][0]*stockDict[goodStock][1]*stockDict[goodStock][2]
        one.append(earnings1)
    else:
        one.append("You haven't invested in this one yet!")
    two = []
    for i in stockDict.keys():
        earnings2 = stockDict[i][0]*stockDict[i][1]*stockDict[i][2]
        if earnings2 > 7000:
            two.append(i)
    two.sort()
    richList = one + two
    return richList
"""
stockDict = {"LLY":(323.86,10,3.98), "ENPH":(277.47,50,-0.72),
             "NBIX":(106.21,100,2.62)}
goodStock = "OXY"
print(theRealDeal(stockDict, goodStock))
"""
"""
stockDict = {"Apple":(138.20,1000,3), "GameStop":(25.13,100,1.3),
             "Google":(96.65,10,1.82), "Amazon":(113,75,1.57)}
goodStock = "Apple"
print(theRealDeal(stockDict, goodStock))
"""
#########################################
"""
Function Name: flightsInfo()
Parameters: flightsDict(dict)
Returns: fixedflightsDict(dict)
"""
def flightsInfo(flightsDict):
    fixedflightsDict = flightsDict.copy()
    for a, b in fixedflightsDict.items():
        idx = 0
        for i in b["passengers"]:
            if len(i) == 2:
                if len(i[0]) >= 0 and len(i[0]) <= 5:
                    i += ("A",)
                    b["passengers"][idx] = i
                elif len(i[0]) == 6:
                    i += ("B",)
                    b["passengers"][idx] = i
                elif len(i[0]) >= 7:
                    i += ("Premium",)
                    b["passengers"][idx] = i
            idx += 1
    return fixedflightsDict                

"""
flightsDict = {"flight1":
               {
                "time":"6:00am",
                "weather":"windy",
                "passengers": [("Farah","20A","A"), ("Jane","4A"),
                               ("Naomi", "3B"),("Fareeda", "1B","Premium'")]
                },
               "flight2":
               {
                   "time":"3:00 pm",
                   "weather":"sunny",
                   "passengers": [("Nelson","2C"), ("Ramya","4A")]
                }
               }
           
print(flightsInfo(flightsDict))
"""
#########################################
"""
Function Name: fastFood()
Parameters: friendDict (dict), menu (dict)
Returns: friendsOwed (list)
"""
def fastFood(friendsDict, menu):
    friendsOwed = []
    for name in friendsDict:
        total = 0
        for choice in friendsDict[name]:
            if choice in menu:
                total += menu[choice]
        friendsOwed.append((name,total))
        friendsOwed.sort()
    return friendsOwed

"""
friendsDict = {
    "Chris": ["coke", "cookie"],
    "Andrew": ["fries", "burger"],
    "Naomi": ["burger"]
    }
menu = {
    "coke": 1.0,
    "fries": 3.0,
    "burger": 10.0,
    "cookie": 2.0,
    }
print(fastFood(friendsDict, menu))
"""











