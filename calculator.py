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