FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    return fahrenheit 

try:
    temp = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if choice.lower() == 'c':
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    elif choice.lower() == 'f':
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    else :
        print("Invalid choice")
except Exception as e:
    print(f"An error occured: {e}")


