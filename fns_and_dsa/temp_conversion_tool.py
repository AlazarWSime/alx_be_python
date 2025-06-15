FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temperature_in_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature_in_celsius

def convert_to_fahrenheit(celsius):
    temperature_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature_in_fahrenheit

def main():
    temperature = float(input("Enter the temperature to convert: "))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
    if temperature_type == 'F':
        print(f"Converted temperature: {convert_to_celsius(temperature):.2f}°C")
    elif temperature_type == 'C':
        print(f"Converted temperature: {convert_to_fahrenheit(temperature):.2f}°F")
    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()