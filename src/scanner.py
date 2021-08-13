import token 

'''
all tokens (for reference)
# single-character tokens
'LEFT_PAREN', 'RIGHT_PAREN', 'LEFT_BRACE', 'RIGHT_BRACE', 
'COMMA', 'DOT', 'MINUS', 'PLUS', 'SEMICOLON', 'SLASH', 'STAR', 

# one or two char tokens
'BANG', 'BANG_EQUAL',
'EQUAL', 'EQUAL_EQUAL',
'GREATER', 'GREATER_EQUAL',
'LESS', 'LESS_EQUAL',

# literals
'IDENTIFIER', 'STRING', 'NUMBER',

# keywords
'AND', 'CLASS', 'ELSE', 'FALSE', 'FUN', 'FOR', 'IF', 'NIL', 'OR',
'PRINT', 'RETURN', 'SUPER', 'THIS', 'TRUE', 'VAR', 'WHILE',
'EOF'
'''

class Scanner():
    
    keywords = {
        'and':'AND',
        'class':'CLASS', 
        'else':'ELSE',
        'false':'FALSE',
        'fun':'FUN',
        'for':'FOR',
        'if':'IF',
        'nil':'NIL',
        'or':'OR',
        'print':'PRINT',
        'return':'RETURN',
        'super':'SUPER',
        'this':'THIS',
        'true':'TRUE',
        'var':'VAR',
        'while':'WHILE'
    }
    
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.line = 1
        self.start = 0
        self.current = 0
        if len(source) > 0:
            self.c = source[self.current]
        else:
            self.c = ''

    def scanTokens(self):
        while not self.atEnd():
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(token.Token('EOF', '\0', None, self.line))
        return self.tokens

    def scanToken(self):
        self.advance()

        if   self.c == '(': self.addToken('LEFT_PAREN') 
        elif self.c == ')': self.addToken('RIGHT_PAREN') 
        elif self.c == '{': self.addToken('RIGHT_BRACE') 
        elif self.c == '}': self.addToken('RIGHT_BRACE') 
        elif self.c == ',': self.addToken('COMMA') 
        elif self.c == '.': self.addToken('DOT') 
        elif self.c == '-': self.addToken('MINUS') 
        elif self.c == '+': self.addToken('PLUS') 
        elif self.c == ';': self.addToken('SEMICOLON') 
        elif self.c == '*': self.addToken('STAR') 
        
        elif self.c == '!': self.addToken('BANG_BANG') \
                            if self.match('!') else self.addToken('BANG')
        elif self.c == '=': self.addToken('EQUAL_EQUAl') \
                            if self.match('=') else self.addToken('EQUAL')
        elif self.c == '<': self.addToken('LESS_EQUAL') \
                            if self.match('=') else self.addToken('LESS')
        elif self.c == '>': self.addToken('GREATER_EQUAL') \
                            if self.match('=') else self.addToken('GREATER')

        elif self.c == '"': self.string()

        elif self.c == ' ': pass
        elif self.c == '\r': pass
        elif self.c == '\t': pass
        elif self.c == '\n': self.line += 1
    
        elif self.c == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.atEnd(): self.advance()
            else:
                self.addToken('SLASH')
        
        else: 
            if (self.c.isdigit()):
                self.digit()
            elif (self.c.isalpha()):
                self.identifier()
            else:
                print('Unexpected token!')

    def string(self):
        while self.peek() != '"' and not self.atEnd():
            if self.peek() == '\n': self.line += 1
            self.advance()
        
        if self.atEnd():
            raise UnterminatedStringError
        
        self.advance()
        value = self.source[self.start+1:self.current-1]
        self.addToken('STRING', value)
        
    def digit(self):
        while self.peek().isdigit(): self.advance()

        if (self.peek() == '.' and self.peek(2).isdigit()):
            self.advance()
            while self.peek().isdigit(): self.advance()
        
        self.addToken('NUMBER', float(self.source[self.start:self.current]))

    def identifier(self):
        while self.isAlphaNumeric(self.peek()): self.advance()
        
        text = self.source[self.start:self.current]
        toktype = Scanner.keywords.get(text, None)
        self.addToken(toktype)

    def isAlphaNumeric(self, c):
        return c.isalpha() or c.isdigit()

    def advance(self):
        # print('IN ADVANCE: ' + str(self.start) + ' ' + str(self.current))
        self.c = self.source[self.current]
        self.current += 1
    
    def addToken(self, TokenType, literal=None):
        # print('IN ADDTOKEN ' + str(self.start) + ' ' + str(self.current))
        text = self.source[self.start:self.current]
        self.tokens.append(token.Token(TokenType, text, literal, self.line))
        
    def atEnd(self):
        #print('IN IS ATEND: ' + str(self.start) + ' ' + str(self.current))
        return self.current >= len(self.source)

    def match(self, expected):
        if self.atEnd(): return False 
        if (self.source[self.current] != expected): return False
        self.current += 1
        return True
    
    def peek(self, lookahead=1):
        if self.current+lookahead-1 >= len(self.source): return '\0'
        return self.source[self.current+lookahead-1]
