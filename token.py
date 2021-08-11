
class Token:
    def __init__(self, toktype, lexeme, literal, line):
        self.toktype = toktype
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def toString():
        return self.toktype + ' ' + lexeme + ' ' + literal
