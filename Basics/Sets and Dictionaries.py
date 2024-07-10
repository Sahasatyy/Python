#Sets
num = {1, 4, 5 ,5 ,6, 6, 7} #This is a set and only prints the unique elements.
num2 = {1, 2, 3, 4, 5, 6}
print(num)
print(num2)
print(num.add(23))
print(num.difference(num2))
print(num.intersection(num2))
print(num.union(num2))
a = set() #Empty set
print(a, type(a))

#Dictionaries
data = {"name":"sahas", "age": "19", "college": "Islington", "Dream": "Developer"}
print(data["Dream"])

Marks = {"sahas": 89, "sohil": 78, "srijan": 87, "amosh": 60}
print(Marks)
Marks["roshan"] = 70 #Add new key value pairs
print(Marks)
print(Marks.pop("sohil")) #Removes specific element from the dictionary
print(Marks)
print(Marks.get("sahas"))
print(Marks.get("sahas Amatya")) #Does not show error just outputs none if no key is found
#print(Marks["Sahas Amatya"]) #Throws error
print(Marks.keys()) #Shows all the keys
print(Marks.values())# Shows all the values
print(Marks.items())# Shows all the key value pairs in tuples"