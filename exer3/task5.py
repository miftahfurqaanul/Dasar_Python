# List of temperatures in Celsius
celsius_temps = [20, 25, 30, 15, 22]

# Use a loop to convert each temperature to Fahrenheit
for celsius in celsius_temps:
    fahrenheit = (celsius * 9/5) + 32  # Convert to Fahrenheit
    print(f"Original: {celsius}°C, Converted: {fahrenheit}°F")