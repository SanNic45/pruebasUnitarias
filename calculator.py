class Calculator:
    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return x / y

    def multiply(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Operands must be numbers.")
        return x * y

    def sum(self, x, y, z):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Operands must be numbers.")
        return x + y + z

    def subtract(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Operands must be numbers.")
        return x - y
