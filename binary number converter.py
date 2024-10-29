def decimal_to_binary_4bit(num):
    # Convert to binary and format to 4 bits
    return format(num, '04b')

# Get user input
try:
    user_input = int(input("Enter a number between 0 and 15: "))
    
    if 0 <= user_input < 16:
        binary_str = decimal_to_binary_4bit(user_input)
        print(f"The 4-bit binary representation of {user_input} is: {binary_str}")
    else:
        print("Error: Please enter a number between 0 and 15.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")

