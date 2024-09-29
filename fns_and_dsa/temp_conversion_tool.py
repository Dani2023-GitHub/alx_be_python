FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELSIUS_T0_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELCIUS_FACTOR*(fahrenheit-32)
    return celsius

def convert_to_fahrenheit(celcius):
    fahrenheit = CELSIUS_T0_FAHRENHEIT_FACTOR * celcius +32
    return fahrenheit

try:
    temp = float(input("Enter the temperature to convert: "))
    choice = input("Is the temperature in Celcius or Fahrenheit?(C/F): ")
    if choice.lower() == 'c':
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    elif choice.lower() == 'f':
        print(f"{temp}°F is {convert_to_celcius(temp)}°C")
    else :
        print("Invalid choice")
except Exception as e:
    print(f"An error occured: {e}")


