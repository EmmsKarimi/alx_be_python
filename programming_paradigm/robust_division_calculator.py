def safe_divide(numerator, denominator):
    try:
        # Convert inputs into float
        num = float(numerator)
        denom = float(denominator)
        
        # Check for division error
        if num == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division 
        result = num / denom
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."