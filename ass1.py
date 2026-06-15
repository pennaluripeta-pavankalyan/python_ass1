# Create a list containing 5 different cities
cities = ["Hyderabad", "Mumbai", "Chennai", "Bangalore", "Delhi"]

# Access and print the city at the middle index
middle_index = len(cities) // 2
print("City at middle index:", cities[middle_index])

# Extract and print the first 3 cities using slicing
first_three = cities[:3]
print("First 3 cities:", first_three)

# Sort the list in ascending order and print
cities.sort()
print("Sorted cities:", cities)

# Append a new city and print the updated list
cities.append("Kolkata")
print("After appending a city:", cities)

# Remove the first city and print the updated list
cities.pop(0)
print("After removing the first city:", cities)

# Function to return the length of a list of cities
def city_list_length(city_list):
    return len(city_list)

# Test the function and print the result
length = city_list_length(cities)
print("Length of the city list:", length)