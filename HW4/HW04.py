"""
Georgia Institute of Technology - CS1301
HW03 -  Loops and Iteration
"""
#########################################
"""
Function Name: decodeString()
Parameters: encodedStr(str)
Returns: decodedList(list)
"""
def decodeString(encodedStr):
    backwards = encodedStr[::-1]
    replace = backwards.replace("@","")
    replace = replace.lower()
    decodedList = replace.split("#")
    return decodedList

#print(decodeString("a@b@#cde@!#!"))
#print(decodeString("J@ckets#1301#!"))
    
#########################################
"""
Function Name: goodBrunch()
Parameters: ashList(list), nickList (list)
Returns: brunchDecision(list)
"""
def goodBrunch(ashList, nickList):
    brunchDecision = [element for element in ashList if element in nickList]
    brunchDecision.sort()
    length = len(brunchDecision)
    if length == 0:
        return "Brunch at home it is!"
    elif length == 1:
        return brunchDecision[0]
    else:
        return brunchDecision

#print(goodBrunch(["Le Bon Nosh", "Petit Chou"], ["Le Bon Nosh", "Bread and Butterfly"]))
#print(goodBrunch(["Butter Milk Kitchen", "Little Tart", "Petit Chou"], ["Little Tart", "Atlanta Breakfast Club", "Butter Milk Kitchen"]))
    
#########################################
"""
Function Name: room_dist()
Parameters: dormMap (list), name1 (str), name2 (str)
Returns: distance (int)
"""
def room_dist(dormMap, name1, name2):
    length = len(dormMap)
    i = 0
    while i < length:
        for element in dormMap[i]:
            if element == name1:
                name1_ind = i
            if element == name2:
                name2_ind = i
        i += 1
    distance = abs(name1_ind - name2_ind)
    return distance

"""       
dormMap = [
    ["Avi", "Rio"], ["Tazio", "Baker"], ["Lesaiah", "Andrew"], ["Robin", "Avery"]
]

print(room_dist(dormMap, "Avi", "Andrew"))
print(room_dist(dormMap, "Tazio", "Baker"))
"""
#########################################
"""
Function Name: freshProduce()
Parameters: veggies (list), prices (list)
Returns: veggieList (list)
"""
def freshProduce(veggies, prices):
    veggieList = []
    empty = []
    total = 0
    for i in range(len(prices)):
        if prices[i] < 4.0:
            total += prices[i]
            veggieList.append(veggies[i])
        else:
            continue
    veggieList.append(total)
    if veggieList == [0]:
        return empty
    else:
        return veggieList

"""
veggies = ["Potato", "Onion", "Shallot", "Basil"]
prices = [3.0, 2.9, 4.3, 6]
veggies = ["Cucumber", "Mushroom", "Broccoli", "Zucchini", "Carrot"]
prices = [1.2, 5.5, 3.7, 2.5, 3.9]
print(freshProduce(veggies, prices))
"""
#########################################
"""
Function Name: find_roommate()
Parameters: my_interests(list), candidates (list), candidate_interests(list)
Returns: match (list)
"""
def find_roommate(my_interests, candidates, candidate_interests):
    list1 = []
    for p in range(len(candidate_interests)):
        similar = 0
        for j in candidate_interests[p]:
            if j in my_interests:
                similar += 1
        if similar >= 2:
            list1.append(candidates[p])
    return list1

    
"""
my_interest = ["baseball", "movie", "e sports", "basketball"]
candidates = ["Josh", "Chris", "Tici"]
candidate_interests = [["movie", "basketball", "cooking", "dancing"],
                ["baseball", "boxing", "coding", "trick-o-treating"],
                ["baseball", "movie", "e sports"]]
print(find_roommate(my_interest, candidates, candidate_interests))
"""






















    
