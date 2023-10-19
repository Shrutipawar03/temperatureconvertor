def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


while True:
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")


    choice = int(input("Enter your choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {result}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {result}°C")
    elif choice == 7:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
