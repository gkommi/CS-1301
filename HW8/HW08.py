"""
Georgia Institute of Technology - CS1301
HW08 - CSV Files/APIs
"""
#########################################
"""
Function Name: fallActivites() 
Parameters: fileName(str), interestedList(list), month(str), minimumRatio(float) 
Returns: greatestTupule(tuple) 
"""
def fallActivities(fileName, interestedList, month, minimumRatio):
    f = open(fileName, "r")
    header = f.readline()
    line_list = f.readlines()
    f.close()
    
    newDict = {}
    for item in line_list:
        item.strip()
        item_list = item.split(",")
        item_tup = tuple(item_list)
        ratio = (int(item_tup[1])) / (int(item_tup[2]))
        newDict[item_tup[0]] = (int(ratio), item_tup[3].strip(), item_tup[0])
    
    list1 = []
    for key in newDict:
        if newDict[key][1] == month and newDict[key][0] >= minimumRatio:
            list1.append(newDict[key])
    list1.sort()
    list1.reverse()
    if len(list1) == 0:
        return "No activities this month!"
    else:
        n = list1[0][2]
        r = list1[0][0]
        greatestTupule = (n, r)
        return greatestTupule

"""
filename = "activity.csv"
interestedList = ["pumpkin patch", "trick or treating", "jump in leaves",
                  "drink chai latte", "visit haunted house","make caramel apples"]
month = "October"
minimumRatio = 35.0
print(fallActivities("activity.csv", interestedList, month, minimumRatio))
"""
#########################################
"""
Function Name: funFallFavs() 
Parameters: fileName (str), letter (str) 
Returns: monthDict (dict) 
"""
def funFallFavs(fileName, letter):
    f = open(fileName, "r")
    header = f.readline()
    line_list = f.readlines()
    f.close()
    monthDict = {}
    newDict = {}
    for item in line_list:
        item.strip()
        item_list = item.split(",")
        item_tup = tuple(item_list)
        ratio = (int(item_tup[1])) / (int(item_tup[2]))
        newDict[item_tup[0]] = (item_tup[3].strip())
    o_count = 0
    s_count = 0
    n_count = 0
    for key in newDict:
        if letter.lower() in key:
            if newDict[key] == "October":
                o_count += 1
            if newDict[key] == "September":
                s_count += 1
            if newDict[key] == "November":
                n_count += 1
        else:
            continue
    list1 = [("September", s_count), ("October", o_count), ("November", n_count)]    
    for tups in list1:
        if tups[1] != 0:
            monthDict[tups[0]] = tups[1]
        else:
            continue
    if len(monthDict) == 0:
        return "Letter not found."
    else:
        return monthDict
"""
fileName = "activity.csv"
letter = "t"
print(funFallFavs(fileName, letter))
"""
#########################################
"""
Function Name: shareBorder() 
Parameters: country1 (str), country2 (str) 
Returns: areNeighbors (bool) 
"""
def shareBorder(country1, country2):
    import requests
    url1 = "https://restcountries.com/v2/name/"+country1.lower()
    url2 = "https://restcountries.com/v2/name/"+country2.lower()
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    data1 = r1.json()
    data2 = r2.json()
    
    try:
        list1 = data1[0]['borders']
        list2 = data2[0]['borders']
        c1 = data1[0]['alpha3Code']
        c2 = data2[0]['alpha3Code']
        #print(list1)
        #print(list2)
        if c1 in list2 or c2 in list1:
            return True
        else:
            return False
    except:
        return False

#print(shareBorder("Iceland", "Canada"))
#########################################
"""
Function Name: currencyRatio() 
Parameters: continent (str), currency (str) 
Returns: ratio (float) 
"""
def currencyRatio(continent, currency):
    import requests
    url = "https://restcountries.com/v2/all"
    r = requests.get(url)
    data = r.json()
    c1 = 0
    c2 = 0
    for d in data:
        if d['region'] == continent:
            c1 += 1
            for curr_d in d['currencies']:
                if curr_d['name'] == currency:
                    c2 += 1
    ratio = round((c2 / c1), 2)
    return ratio
    
#print(currencyRatio("Americas", "United States dollar"))


"""
    all_url = "https://restcountries.com/v2/all"
    r1 = requests.get(all_url)
    all_data = r1.json()
    
    for country in all_data:
        if country['currencies'][0]['name'].lower() == currency.lower():
            currency_code = country['currencies'][0]['code']
            break
    print(currency_code)
    currency_counter = 0
    currency_url = "https://restcountries.com/v3.1/currency/"+currency_code
    print(currency_url)
    r2 = requests.get(currency_url)
    currency_data = r2.json()
    for country in currency_data:
        try:
            #print(country["currencies"][0]['code'])
            key_list = country['currencies'].keys()
            print(key_list)
            key1 = key_list[0]
            print(key1)
            if currency.lower() == country['currencies'][key1]['name'].lower():
                currency_counter += 1
        except:
            continue
    print(currency_counter)
    
    continent_url = "https://restcountries.com/v3.1/region/"+continent.lower()
    r2 = requests.get(continent_url)
    cont_data = r2.json()

    print(len(cont_data))
"""
#########################################
"""
Function Name: countriesInfo()
Parameters: countriesList (list)
Returns: None(NoneType)
"""
def countriesInfo(countriesList) :
    import requests
    f = open("countries.csv", "w")
    f.write("Country,Capital,Population,Languages,Currencies")
    for country in countriesList:
        try:
            url = "https://restcountries.com/v2/name/{}".format(country.lower())
            r = requests.get(url)
            data = r.json()
            f.write("\n" + country + "," + data[0]["capital"] + "," + str(data[0]['population']) + ",")
            for i in range(len(data[0]['languages'])):
                f.write(data[0]['languages'][i]['name'])
                if i != len(data[0]['languages']) - 1:
                    f.write('-')
                else:
                    f.write(',')
            for i in range(len(data[0]['currencies'])):
                f.write(data[0]['currencies'][i]['name'])
                if i != len(data[0]['currencies']) - 1:
                    f.write('-')
        except:
            continue
    f.close()
    
    
#countriesInfo(["Canada", "Cuba"])

"""  
    import requests
    import pprint

    f = open("countries.csv", "w")
    if len(countriesList) == 0:
        f.write("Country,Capital,Population,Languages,Currencies")
    else:
        f.write("Country,Capital,Population,Languages,Currencies\n")

    count = 0    
    for country in countriesList:
        count += 1
        url = "https://restcountries.com/v2/name/{}".format(country.lower())
        r = requests.get(url)
        data = r.json()
        typ = type(data)

        if typ == list:
            cap = "," + data[0]['capital']
            pop = "," + str(data[0]['population'])
            if len(data[0]['languages']) != 1:
                lang_string = ""
                for i in range(len(data[0]['languages'])):
                    lang_string += "-" + data[0]['languages'][i]['name']              
                    lang = "," + lang_string[1:]            
            else:
                lang = "," + data[0]['languages'][0]['name']

            if len(data[0]['currencies']) != 1:
                curr_string = ""
                for i in range(len(data[0]['currencies'])):
                    curr_string += "-" + data[0]['currencies'][i]['name']              
                    curr = "," + curr_string[1:]            
            else:
                curr = "," + data[0]['currencies'][0]['name']   

            if count == len(countriesList):
                f.write(country + cap + pop + lang + curr)
            else:
                f.write(country + cap + pop + lang + curr + "\n")
        else:
            continue
    f.close()
    
countriesInfo(["Canada", "Cuba"])
"""
