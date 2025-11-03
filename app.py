import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index,item in enumerate(data):
    print(index, ":", (item)["title"])
    

choice = int(input("Give a year:"))
for i in enumerate (data):
    if (item)["year"] > choice:
         print((item)["title"])
