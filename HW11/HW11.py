"""
Georgia Institute of Technology - CS1301
HW11
"""
#########################################
"""
Function Name: santaHelper()
Parameters: kids (list)
Returns:  destinations (dict)
"""
def santaHelper(kids):
    if len(kids) == 0:
        return {}
    else:
        if kids[0][1] == True:
            destinations = santaHelper(kids[1:])
            if kids[0][2] in destinations:
                destinations[kids[0][2]].append(kids[0][0])
                destinations[kids[0][2]].sort()
            else:
                destinations[kids[0][2]] = []
                destinations[kids[0][2]].append(kids[0][0])
                destinations[kids[0][2]].sort()
            return destinations
        elif kids[0][1] == False:
            destinations = santaHelper(kids[1:])
            return destinations
"""
#kids = [("Ralph", True, "Houston"),("Bailey", False, "New York"),("Bill", True, "San Francisco")]
kids = [("Joe", True, "New York"),("Aiden", True, "Atlanta"),("Emma", True, "New York")]
print(santaHelper(kids))
"""  
#########################################
"""
Function Name: myWishlist()
Parameters: stores (dict)
Returns: None (NoneType)
"""
def myWishList(stores):
    f = open("wishlist.txt", "w")
    if len(stores) == 0:
        f.write("My WishList")
    else:
        f.write("My WishList\n")
        dict1 = {}
        for key in stores:
            for (item,price) in stores[key]:
                if item not in dict1:
                    dict1[item] = [(price, key)]
                else:
                    dict1[item].append((price,key))
                    dict1[item].sort()
        
        list1 = dict1.keys()
        for (index,key) in enumerate(list1):
            if index != 0:
                f.write("\n\n"+key+":\n")
                for i in range(len(dict1[key])):
                    f.write("\n"+dict1[key][i][1])
            else:
                f.write("\n"+key+":\n")
                for i in range(len(dict1[key])):
                    f.write("\n"+dict1[key][i][1])
    f.close()
"""
#stores = {"Nordstrom":[("Jacket",53),("Hat",61)],"Bloomingdales":[("Jacket",46),("Hat",89),("Shoes",77)]}
stores = {"Apple": [("MacBook",2000),("iPhone14",1500)],"Barnes and Nobles":[("GTMerch",300000000),("MacBook",2200)]}
myWishList(stores)
"""
#########################################
"""
Function Name: getMessage()
Parameters: presaleCode (int)
Returns: message (str)
"""
def getMessage(presaleCode):
    conversion_table = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    message = ''
    while(presaleCode > 0):
        remainder = presaleCode % 16
        message = conversion_table[remainder] + message
        presaleCode = presaleCode // 16
    return message

#print(getMessage(12648430))    
#########################################
"""
Function Name: buildFrosty()
Parameters: materials (dict)
Returns: snowManStr (str)
"""
def buildFrosty(materials):
    dict1 = {}
    for name in materials:
        for material in materials[name]:
            if material not in dict1:
                dict1[material] = materials[name][material]
            else:
                dict1[material] += materials[name][material]
    #print(dict1)
    sticks = dict1["sticks"]
    rocks = dict1["rocks"]
    carrots = dict1["carrot"]
    hats = dict1["hat"]
    if sticks<2 or rocks<10 or carrots<1 or hats<1:
        return "Not enough materials :("
    else:
        return "We have enough materials to build the snowman :)"

"""  
materials = {"Cynthia": {"sticks": 5, "rocks": 3, "carrot": 1},
             "Harshith": {"carrot": 1, "scarf": 1, "socks": 3, "rocks": 3},
             "Josh": {"rocks": 2, "buttons": 3, "hat": 1}}
             
materials = {"Ramya": {"sticks": 1, "rocks": 3, "hat": 1},
              "Jane": {"carrot": 1, "scarf": 1, "shoes": 2, "rocks": 8},
              "Anastasiya": {"sticks": 2, "buttons": 3, "carrot": 10}}
print(buildFrosty(materials))
"""
#########################################
"""
Function Name: guideBuddy()
Parameters: locationDict(dict), movementsList(list)
Returns:  newRoutine (str)
"""
def guideBuddy(locationDict, movementsList):
    from HW11 import distance
    x = 0
    y = 0
    for direction in movementsList:
        if direction == "right":
            y += 1
        elif direction == "left":
            y -= 1
        elif direction == "up":
            x += 1
        elif direction == "down":
            x -= 1
    position = [x,y]
    
    list1 = []
    for location in locationDict:
        dist = distance(position, locationDict[location])
        list1.append((dist, location))

    list1.sort()
    print(list1)
    loc = list1[0][1]
    return "Go to {}!".format(loc)

## helper method for guideBuddy
## alist and blist are lists of length 2 containing locations
import math
def distance(alist, blist):
    return math.sqrt((alist[0] - blist[0])**2 + (alist[1] - blist[1])**2)
"""
locationDict = {"Central Park": [3,4], "Empire State Building": [-2,4],
                "Statue of Liberty": [-1, 5], "Rockefeller Center": [4, 1]}
movementsList = ["right", "left", "left", "left", "up", "up", "up", "left", "left"]
print(guideBuddy(locationDict,movementsList))
"""























