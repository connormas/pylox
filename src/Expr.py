
class Expr():
    def __init__(self):
        pass


class Binary(Expr):
    def __init(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Grouping(Expr):
    def __init(self, expression):
        self.expression = expression


class Literal(Expr):
    def __init(self, value):
        self.value = value


class Unary(Expr):
    def __init(self, operator, right):
        self.operator = operator
        self.right = right


