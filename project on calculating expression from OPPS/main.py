class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression
        self.result = None

    def solve(self):
        try:
            self.result = eval(self.expression)
        except Exception as e:
            self.result = f"Error: {e}"

    def display_result(self):
        print(f"Expression: {self.expression}")
        print(f"Result: {self.result}")


# Example usage
expr = input("Enter a mathematical expression: ")
solver = ExpressionSolver(expr)
solver.solve()
solver.display_result()