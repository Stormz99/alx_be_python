# Global conversion tool for temperature units
FAHRENHEIT_TO_CELSUIS_FACTOR = 5 / 9
CELSUIS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsuis(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSUIS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSUIS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        unit = input("Is this temperature in Celsuis or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "f":
            converted = convert_to_celsuis(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        elif unit == "c":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsuis or 'F' for Fahrenheit")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        

if __name__ == "__main__":
    main()