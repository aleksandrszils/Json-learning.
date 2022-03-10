import json

file = open("students.json")
data = json.load(file)

for student in data["Students"]:
    print(student["FirstName"])

#KOMANDAS UZDEVUMS 1
#Atrodi vidējo studentu vecumu (Age)
count = 0
total_age = 0
for student in data["Students"]:
    count += 1
    total_age += int(student["Age"])

print(f"Average age: {total_age/count}")