#V1.0
#power
def calculate_power():
    base = int(input("Enter the base Number: "))
    exponent = int(input("Enter the Exponent Number: "))
    try:
        base = float(base)
        exponent = int(exponent)
        result = base ** exponent
        print(f'result: {int(result)}')
    except ValueError:
        print("Invalid input. Please enter numberic Values.")

calculate_power()

#division
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b
    
    
