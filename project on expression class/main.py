class Expression:
    def __init__(self, expression: str):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"

    def print_result(self):
        result = self.solve()
        print(f"The result of '{self.expression}' is: {result}")

if __name__ == "__main__":
    expr_input = input("Enter a mathematical expression: ")
    expr = Expression(expr_input)
    expr.print_result()