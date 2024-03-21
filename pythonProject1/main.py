# Task 1: List Comprehensions
squares = [x ** 2 for x in range(1, 11)]
print("Task 1:", squares)

# Task 2: Functions
def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]

print("Task 2:", generate_squares(1, 10))

# Task 3: Classes
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]

generator = SquareGenerator()
print("Task 3:", generator.generate_squares(1, 10))