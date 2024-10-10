# Function to print a personalized greeting
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Test the function with different names and greetings
greet("Alice")  # Uses the default greeting
greet("Bob", "Hi")
greet("Charlie", "Good morning")
greet("Dana")  # Uses the default greeting
greet("Eve", "Greetings")