from lexer import TOKEN_TYPE_DICT
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance() # Need advance to start going through the list

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
        """The expression rule considers the add and subtract operations.
        It looks through all add and subtract tokens, and keeps 
        adding add or subtract nodes to the term. It returns the 
        final term with all the recursive nodes.
        """
        result = self.term() # get first half of expression

        # loop through all + or - tokens
        while self.current_token is not None and \
            self.current_token.type in ("PLUS", "MINUS"):
            if self.current_token.type == "PLUS":
                self.advance() # change current token
                result = AddNode(result, self.term())
            elif self.current_token.type == "MINUS":
                self.advance() # change current token
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        """The term rule considers the multiply and divide operations.
        It looks through all multiply and divide tokens, and keeps 
        adding multiply or divide nodes to the term. It returns the 
        final term with all the recursive nodes.
        """

        result = self.factor() # get first half of term

        # loop through all * or / tokens
        while self.current_token is not None and \
            self.current_token.type in ("MULTIPLY", "DIVIDE"):
            if self.current_token.type == "MULTIPLY":
                self.advance() # change current token
                result = MultiplyNode(result, self.term())
            elif self.current_token.type == "DIVIDE":
                self.advance() # change current token
                result = DivideNode(result, self.term())

        return result

    def factor(self):
        """The factor rule takes in a number token, moves to the next
        token, and returns a number node of the first token.
        """

        token = self.current_token

        if token.type == "NUMBER":
            self.advance() # change current token
            return NumberNode(token.value)

        # Not a number token so most likely error since we are supposed 
        # to alternate between numbers and operators
        self.raise_error()
