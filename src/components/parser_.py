from .types.tokens import TokenType
from .types.nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance() # Need advance to reach the first token

    def raise_error():
        raise Exception("Invalid Syntax")

    def advance(self):
        """Move to next token"""
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        """Takes in an iterator  of tokens and returns an expression.
        The expression is a node that represents an operator. Each node
        can have other operator nodes inside them.
        """

        # No user input
        if self.current_token is None:
            return None

        #perform expression rule
        result = self.expr()

        # Expression rule did not understand input, syntax error
        if self.current_token is not None:
            self.raise_error()

        return result

    def expr(self):
        """The expression rule considers the + and - operations. It 
        looks through all + and - tokens, and keeps  adding + or - nodes
        to the term. It returns the final term with all the recursive 
        nodes.
        """
        result = self.term() # get first half of expression

        # loop through all + or - tokens
        while self.current_token is not None and \
            self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance() # skip past + token
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance() # skip past - token
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        """The term rule considers the *, / and % operations. It looks 
        through all *, / and % tokens, and keeps adding *, / and % nodes
        to the term. It returns the final term with all the recursive 
        nodes.
        """

        result = self.exp() # get first half of term

        # loop through all * or / tokens
        while self.current_token is not None and \
            self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance() # skip past * token
                result = MultiplyNode(result, self.term())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance() # skip past / token
                result = DivideNode(result, self.term())
            elif self.current_token.type == TokenType.MODULO:
                self.advance() # skip past % token
                result = ModuloNode(result, self.term())

        return result

    def exp(self):
        """The exp rule considers the ^ operation. It looks 
        through all ^ tokens, and keeps adding ^ nodes to 
        the term. It returns the final term with all the recursive nodes.
        """

        result = self.factor() # get first half of term

        # loop through all * or / tokens
        while self.current_token is not None and \
            self.current_token.type == TokenType.EXPONENT:
            if self.current_token.type == TokenType.EXPONENT:
                self.advance() # skip past ^ token
                result = ExponentNode(result, self.term())

        return result

    def factor(self):
        """The factor rule takes in a token and returns the appropriate
        node. For a number token, it moves to the next token, and 
        returns a number node with the value of the first token. If it 
        encounters a + or - token, it calls itself to act as a unary
        operator and returns a unary node. If it encounters a (, it 
        calls the experssion function to get an expression node.
        """

        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance() # skip past ( token
            result = self.expr() # find the whole expression

            if self.current_token.type != TokenType.RPAREN:
                self.raise_error()

            self.advance() # skip past ) token
            return result
        
        elif token.type == TokenType.NUMBER:
            self.advance() # move to next token (operator)
            return NumberNode(token.value)
        
        elif token.type == TokenType.PLUS:
            self.advance() # skip past + token
            # call factor function again to act as unary operator
            return PlusNode(self.factor()) 
        elif token.type == TokenType.MINUS:
            self.advance() # skip past - token
            # call factor function again to act as unary operator
            return MinusNode(self.factor())

        # Not a number token so most likely error since we are supposed 
        # to alternate between numbers and operators
        self.raise_error()
