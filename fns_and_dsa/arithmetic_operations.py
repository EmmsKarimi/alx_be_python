def perform_operation(num1, num2, operation):
    """
    perform basic arithmetic operations.
    
    parameters:
    - num1 (float): The first number:
    - num2 (float): The second number:
    - operation (str): The operation to perform (add, subtract, multiply, divide)
    
    Returns:
    - float or str: The result of the operation or an error message.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtarct":
        return num1 - num2 
    elif operation == "multiply":
        return num1 * num2 
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid opertation."