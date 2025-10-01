capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart","Berlin"],

}


# Pause 1: Printing out 'Lille'
print(travel_log["France"][1])


# Nested lists
# This is an example of a 2D list
nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

# Nesting a Dictionary inside a Dictionary

travel_log.clear()
travel_log = {
    "France": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany":{
        "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    }
}

print(travel_log["Germany"]["cities_visited"][2])