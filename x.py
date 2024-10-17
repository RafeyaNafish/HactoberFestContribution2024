def smallest_x_digit_number(x):
    if x < 1:
        return "Invalid input. x must be 1 or greater."
    return 10 ** (x - 1)

# Example usage:
x = 3  # Change this value to find the smallest x-digit number for different x
result = smallest_x_digit_number(x)
print(f"The smallest {x}-digit number is: {result}")
