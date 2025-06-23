def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        else:
            result = numerator/denominator
            return(result)
    except ValueError as e:
        print(f"Please enter numeric values only")    
    except ZeroDivisionError as e:
        print(e)
        return 