cities = {
    "New York": 8622390,
    "London": 8981639,
    "Tokyo": 13935081,
    "Paris": 2140520,
    "Shanghai": 24873203
}

# Print each city and population
for city, population in cities.items():
    print(f"{city} has a population of {population}.")

# Identify and print the city with the largest population
largest_population = max(cities.values())
for city, population in cities.items():
    if population == largest_population:
        print(f"{city} has the largest population of {largest_population}.")

# Remove a city from the dictionary
cities.pop("Paris")
print("Updated dictionary:", cities)