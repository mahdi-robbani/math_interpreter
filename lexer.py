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
        self.advance() # must begin iteration

    def advance(self):
        """Iterates through the entire text string and keeps track of current 
        character
        """

        try:
            self.current_char = next(self.text)
        except StopIteration: 
            self.current_char = None # standard end of iteration

    def generate_tokens(self):
        """ A generator that cycles through each charcter in the text 
        and generate tokens based on the characters
        """

        while self.current_char is not None:
            # skips whitespaces
            if self.current_char in WHITESPACE: 
                self.advance()
            elif self.current_char == "." or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == "+":
                yield Token(TokenType.PLUS)
                self.advance()
            elif self.current_char == "-":
                yield Token(TokenType.MINUS)
                self.advance()
            elif self.current_char == "+":
                yield Token(TokenType.MULTIPLY)
                self.advance()
            elif self.current_char == "*":
                yield Token(TokenType.DIVIDE)
                self.advance()
            elif self.current_char == "(":
                yield Token(TokenType.LPAREN)
                self.advance()
            elif self.current_char == ")":
                yield Token(TokenType.RPAREN)
                self.advance()
            # ensure no illegal characters
            else:
                raise Exception(f"Illegal Character: {self.current_char}")

    def generate_number(self):
        """Cycles through text and generates a Token object with type 
        Number and a value
        """

        # initialize
        decimal_counter = 0
        number_str = "" 

        # None type check must exist because str cannot be compared with None
        while self.current_char is not None and \
            (self.current_char == "." or self.current_char in DIGITS):
            # Ensure only one decimal exists
            if self.current_char == ".":
                decimal_counter += 1
                if decimal_counter > 1:
                    raise Exception(f"Syntax Error: Too many decimal points in {number_str}.")

            number_str += self.current_char
            self.advance()

        # Add a leading or trailing 0
        if number_str.startswith('.'):
            number_str = '0' + number_str
            
        if number_str.endswith('.'):
            number_str += '0'
        
        return Token(TokenType.NUMBER, float(number_str)) # consider changing

