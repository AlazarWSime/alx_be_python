def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError
        else:
            result = numerator/denominator
            print(f"The result of the division is {result}")
            return result
    except ValueError as e:
        print("Error: Please enter numeric values only.")    
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Unsupported types for division.")