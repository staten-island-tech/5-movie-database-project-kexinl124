import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index,item in enumerate(data):
    print(index, ":", (item)['title'])
    

choice1 = int(input("Give a year after:"))
choice2 = int(input("Give a year for before:"))
choice3=int(input("Choose a specific year"))
for item in data:
    if choice2 > item['year'] > choice1:
         print(item["title"])
    else:
        choice3=item['year']
        print(item['title'])
        

