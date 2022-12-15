"""
Georgia Institute of Technology - CS1301
HW05 -  Lists, Tuples, and Modules
"""
#########################################
"""
Function Name: teamPicker()
Parameters: sportInterests (list), intramural (str)
Returns: team (list)
"""
def teamPicker(sportInts, intra):
    team = []
    for i in range(len(sportInts)):
        if intra in sportInts[i][1]:
            team.append(sportInts[i][0])
    team.reverse()
    if len(team) == 0:
        return "Free agent :/"
    else:
        return team

"""
sportsInterests = [('Timothy', ['Basketball', 'Tennis', 'Badminton']),('Mo', ['Tennis', 'Ping Pong', 'Dodgeball']),('Ashley', ['Sand Volleyball', 'Volleyball'])]
intramural = "Tennis"
print(teamPicker(sportsInterests, intramural))
"""
#########################################
"""
Function Name: vacationPlanner()
Parameters: trips (list), costs (list)
Returns: vacationSpots (tuple)
"""
def vacationPlanner(trips, costs):
    list1 = list(zip(trips, costs))
    list1.sort()
    list2 = []
    emptyList = []
    costs.sort()
    
    if len(costs) == 0:
        list2.append("")
        list2.append(emptyList)
        vacationSpots = tuple(list2)
    else:
        minCost = costs[0]
        for i in range(len(list1)):
            for p in list1[i]:
                if minCost == p:
                    list2.append(list1[i][0])
        list2.sort()
        list2.append(list1)
        vacationSpots = tuple(list2)

    return vacationSpots

"""
trips = ['China', 'England', 'Australia', 'Japan', 'India']
costs = [1200, 800, 1950, 1730, 1500]
print(vacationPlanner(trips, costs))
"""

"""
trips = []
costs = []
print(vacationPlanner(trips, costs))
""" 
#########################################
"""
Function Name: fastFood()
Parameters: foods (list), costs (list)
Returns: friendsOwed (list)
"""

def fastFood(foods, costs):
    list1 = []
    foods.sort()
    for one, first in foods:
        tup1 = ()
        total = 0
        for two, second in foods:
            if one == two:
                for i,cost in costs:
                    if i == second:
                        total += cost
                        break
        tup1 = tup1 + (one,total)
        if tup1 not in list1:
            list1.append(tup1)
    return list1      

"""
foods = [('Chris', 'Burger'), ('Chris', 'Burger'), ('Josh', 'Ice cream'), ('Parul', 'K-dog'), ('Paige', 'Fries')]
costs = [('Ice cream', 1.0), ('Fries', 0.5), ('Burger', 3.0), ('K-dog', 5.0)]
print(fastFood(foods, costs))
"""
#########################################
"""
Function Name: reviewSession()
Parameters: rooms (list), dates (list)
Returns: roomsAvailable (list)
"""
import calendar
def reviewSession(rooms, dates):
    roomsAvailable = []
    year = 2022
    for d in range(len(dates)):
        for date in dates[d]:
            month = dates[d][0]
            day = dates[d][1]
            x = calendar.weekday(year, month, day)
            if x == 3 or x == 4:
                roomsAvailable.append(rooms[d])
            else:
                continue
    roomsAvailable = list(dict.fromkeys(roomsAvailable))
    roomsAvailable.sort()
    return roomsAvailable

"""
rooms = ['CULC 144', 'CULC 152', 'CCB 016', 'Skiles 246']
dates = [(9,30), (10,1),(10,22), (10,21)]
print(reviewSession(rooms, dates))
"""
#########################################
"""
Function Name: esportsBracket()
Parameters: tourneyList (list)
Returns: tourneyWinner (str)
"""
def esportsBracket(tourneyList):
    import esportsMatch
    
    list1 = []
    for (team1, team2) in tourneyList:
        x = team1
        y = team2
        semiwinner = esportsMatch.matchHistory(x, y)
        list1.append(semiwinner)

    x = list1[0]
    y = list1[1]
    finalwinner = esportsMatch.matchHistory(x, y)
    return finalwinner

"""       
tourneyList = [['DRX', 'Optic'], ['Paper Rex', 'Fnatic']]
print(esportsBracket(tourneyList))
"""

aList = ["banana", ["cherry", "apple"]]
bList = aList[1]
cList = aList[:]
cList[0].strip("anana")
stri = "banana".strip("anana")
print(stri)
print(cList)
bList[1] = bList[0].replace("ch", "b")
bList.sort()

print(cList)












