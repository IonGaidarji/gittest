people = [
    {"name": "harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclow"},
    {"name": "Draco", "house": "Slytherin"}
]


people.sort(key= lambda person: person["house"]) #take person as input and return person["name"]

print(people)