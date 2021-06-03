from tokens import Token, TokenType

# constants
WHITESPACE = ' \t\n'
DIGITS = '0123456789'

class Lexer:
    """Class used for converting text to a list of tokens"""

    def __init__(self, text):
        """intilaize the Lexer with some text, and creates an interator
        from that text
        """

        self.text = iter(text)
        self.advance() #???

    def advance(self):
        """Iterates through the entire text string and keeps track of current 
        character
        """

        try:
            self.current_char = next(self.text)
        except StopIteration: # standard end of iteration
            self.current_char = None

    def generate_tokens(self):
        """ A generator that cycles through each charcter in the text 
        and generate tokens based on the characters
        """

        while self.current_char is not None:
            if self.current_char in WHITESPACE: 
                # skips whitespaces
                self.advance()
            elif self.current_char == "." or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == "*":
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == "/":
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == "*":
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal Character: {self.current_char}")

    def generate_number(self):
        """Cycles through text and generates a Token object with type 
        Number and a value
        """

        decimal_counter = 0
        number_str = self.current_char #consider changing
        self.advance()

        while self.current_char is not None and \
            (self.current_char == "." or self.current_char in DIGITS):
            if self.current_char == ".":
                decimal_counter += 1
                if decimal_counter > 1:
                    raise Exception(f"Syntax Error: Too many decimal points")

            number_str += self.current_char
            self.advance()

        # Add a leading or trailing 0
        if number_str.startswith('.'):
            number_str = '0' + number_str
            
        if number_str.endswith('.'):
            number_str += '0'
        
        return Token(TokenType.NUMBER, float(number_str)) # consider changing

