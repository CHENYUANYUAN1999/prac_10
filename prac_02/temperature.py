def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_to_f = convert_to_fahrenheit(celsius)
            print(f"Result: {convert_to_f:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_to_c = convert_to_celsius(fahrenheit)
            print(f"Result: {convert_to_c:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_to_fahrenheit(i):
    fahrenheit = i * 9.0 / 5 + 32
    return fahrenheit

def convert_to_celsius(i):
    celsius = (i - 32) * 5 / 9
    return celsius

main()