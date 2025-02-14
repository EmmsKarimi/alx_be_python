# explore_datetime.py
from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the result
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user for input
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the result
    print(f"Future date: {formatted_future_date}")


# Main program
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
