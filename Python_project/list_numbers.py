numbers = []
print("Please enter 3 numbers (each must be less than or equal to 100):")

for i in range(3):
    number = int(input(f"Enter number {i + 1}: "))

    if number <= 100:
        numbers.append(number)
    else:
        print("Error: Number cannot be greater than 100.")

print("The sum is:", sum(numbers))
