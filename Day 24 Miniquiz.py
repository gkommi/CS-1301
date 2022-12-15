def write_stuff(file, string):
    f = open(file, "w")
    list1 = string.split()
    #print(list1)
    for word in list1:
        f.write(word + "\n")

#write_stuff("day24miniquiz.txt", "My favorite class is CS1301!")
        
flavors = {"blue": ("blueberries", 4.50), "brown": ("cocoa powder", 2.00)}
print(flavors.items())

print(len(('blue', 0)))
