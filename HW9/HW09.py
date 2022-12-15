"""
Georgia Institute of Technology - CS1301
HW09 -  Recursion
"""
#########################################
"""
Function Name: hoursWorked()
Parameters: clockedHours (list)
Returns:  totalHours (int)
"""
def hoursWorked(clockedHours):
    count = 0
    if len(clockedHours) == 0:
        return 0
    else:
        count += clockedHours[0]
        return count + hoursWorked(clockedHours[1:])

#print(hoursWorked([1,3,6,12]))
#########################################
"""
Function Name: secretLocation()
Parameters: location (str)
Returns: decodedLocation (str)
"""
def secretLocation(location):
    if len(location) == 0:
        return ''
    else:
        if location[0].islower() == False and location[0] != ' ':
            return secretLocation(location[1:])
        else:
            return location[0] + secretLocation(location[1:])
        
#print(secretLocation("!cSKu1lL3c$"))
#########################################
"""
Function Name: springRegistration()
Parameters: originalCRNs (list)
Returns: finalCRNs (list)
"""
def springRegistration(crn):
    final = []
    if len(crn) == 0:
        return final
    else:
        if crn.count(crn[0]) >= 2:
            return springRegistration(crn[1:])
        else:
            list1 = [crn[0]]
            return list1 + springRegistration(crn[1:])
        
#print(springRegistration([21942, 25594, 22907, 22275]))
        
##########################################
"""
Function Name: poncePlanner()
Parameters: restaurantChoices (list)
Returns: taFavorites (dict)
"""
def poncePlanner(restaurantChoice):
    if len(restaurantChoice) == 0:
        return {}
    else:
        taFavorites = poncePlanner(restaurantChoice[1:])
        taFavorites[restaurantChoice[0][0]] = restaurantChoice[0][1]
        return taFavorites
  
#restaurantChoice = [("Naomi", "Honeysuckle Gelato")]
#restaurantChoice = []
#restaurantChoice = [("Paige", "Dancing Goats"), ("Fareeda", "Botiwala"),
                    #("Ramya", "Minero"), ("Jane", "Pancake Social")]
                    
#print(poncePlanner(restaurantChoice))
#########################################
"""
Function Name: drawRectangle()
Parameters: width (int), height (int)
Returns:  None (NoneType)
"""
def drawRectangle(w, h):
    if w < 3:
        return print("You're cutting corners!")
    if h == 1:
        print('*' * w)
    else:
        if h == w:
            print('*' * w)
        else:
            print('*' + (' ' * (w - 2)) + '*')
        drawRectangle(w, h - 1)

#drawRectangle(2, 4)
    
        





















