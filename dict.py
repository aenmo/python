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
"year":"2005"
}
x=thisdict.get("model")
print(x)

thisdict = {
"brand":"lambo",
"model":"hurrican",
"year":"2000"
}
thisdict["year"] = 2005
print(thisdict)


thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2005"
}
for x in thisdict:
    print(x)
    print(thisdict[x])

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2005"
}
for x in thisdict.values():
    print(x)

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2005"
}
for x,y in thisdict.items():
    print(x,y)

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2005"
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
print(len(thisdict))

thisdict = {
"brand": "lambo",
"model": "hurrican",
"year": "2005"
}
thisdict["color"]="red"
print(thisdict)
