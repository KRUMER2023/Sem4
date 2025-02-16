def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9,2)

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32,2)


print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = input("Choose an option (1/2): ")

if choice == '1':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(fahrenheit,"°F is equal to",fahrenheit_to_celsius(fahrenheit))

elif choice == '2':
    celsius = float(input("Enter temperature in Celsius: "))
    print(celsius,"°C is equal to ",celsius_to_fahrenheit(celsius))

else:
    print("Invalid choice.")
