# Global variable defined outside the function
global_var = "I am miftah furqaanul haq"

# Function that uses the global variable and a local variable
def print_variables():
    # Local variable
    local_var = "I am topa"
    # Print both variables inside the function
    print(f"Global variable: {global_var}")
    print(f"Local variable: {local_var}")

# Test the function
print_variables()

# Print global variable outside the function to show it is accessible
print(f"Global variable outside the function: {global_var}")