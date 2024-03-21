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

# Task 4: Libraries
import math

class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x ** 2 for x in range(start, end + 1)]
        return [math.sqrt(square) for square in squares]

generator = SquareGenerator()
print("Task 4:", generator.generate_squares(1, 10))


# Task 5: Exceptions
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start")
        squares = [x ** 2 for x in range(start, end + 1)]
        return [math.sqrt(square) for square in squares]

generator = SquareGenerator()
try:
    print("Task 5:", generator.generate_squares(1, 0))
except ValueError as e:
    print("Task 5:", e)


# Task 6: Modules
import math


generator = SquareGenerator()
print("Task 6:", generator.generate_squares(1, 10))

# Task 8: Inheritance
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than or equal to start")
        return [x ** 3 for x in range(start, end + 1)]

cubic_generator = CubicGenerator()
print("Task 8:", cubic_generator.generate_squares(1, 10))
