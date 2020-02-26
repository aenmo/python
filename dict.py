thisdict = {
"brand":"lambo",
"model":"hurrican",
"year":"2005"
}
x = thisdict["brand"]
print(x)


thisdict = {
"brand":"lambo",
"model":"hurrican",
"year":"2014"
}
x=thisdict.get("model")
print(x)

thisdict = {
"brand":"lambo",
"model":"hurrican",
"year":"2014"
}
thisdict["year"] = 2005
print(thisdict)


thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2014"
}
for x in thisdict:
    print(x)
    print(thisdict[x])

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2014"
}
for x in thisdict.values():
    print(x)

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2014"
}
for x,y in thisdict.items():
    print(x,y)

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2014"
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2014"
}
thisdict["color"]="red"
print(thisdict)

 #Removing Items
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:

del thisdict["year"]
print(thisdict)

#The del keyword can also delete the dictionary completely:

thisdict.clear()
print(thisdict)


thisdict = {
"brand":"lambo",
"model":"hurrican",
"year":2014
}
thisdict.clear()
print(thisdict)

#Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }

mydict = thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in method dict().
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries
#A dictionary can also contain many dictionaries, this is called nested dictionaries
myfamily = {
"child1" : {
"name" : "elli",
"year" : 2006
},
"child2" : {
"name" : "priya",
"year" : 2007
},
"child3" : {
"name" : "neha",
"year" : 2009
 }
}
print(myfamily)

#Create three dictionaries, than create one dictionary that will contain the other three dictionaries:

child1 = {
"name":"elli",
"year":2008
}
child2 = {
"name":"abram",
"year":2008
}
child3 = {
"name":"neha",
"year":2007
}

myfamily = {
"child1":child1,
"child2":child2,
"child3":child3
}
print(myfamily)

#The dict() Constructor
#It is also possible to use the dict() constructor to make a new dictionary

thisdict=dict(brand="apple",model="ipad 6th gen.",year=2017)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
