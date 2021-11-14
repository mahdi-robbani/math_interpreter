import unittest
from src.components.types.tokens import TokenType, Token
from src.components.parser_ import Parser
from src.components.types.nodes import *

class TestParser(unittest.TestCase):
    """Contains all the tests for the Parser class"""

    def test_empty(self):
        """Ensure empty list of tokens returns None"""

        tokens = []
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, None)

    def test_number(self):
        """Ensure number token returns a number node"""

        tokens = [Token(TokenType.NUMBER, 12.4)]
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, NumberNode(12.4))

    def test_individual_operations(self):
        """Test each individual operation"""

        tokens = [Token(TokenType.NUMBER, 12.4), 
                  Token(TokenType.PLUS), 
                  Token(TokenType.NUMBER, 0.98)]
        
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, AddNode(NumberNode(12.4), NumberNode(0.98)))

        tokens = [Token(TokenType.NUMBER, 12.4), 
                  Token(TokenType.MINUS), 
                  Token(TokenType.NUMBER, 0.98)]
        
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, SubtractNode(NumberNode(12.4), NumberNode(0.98)))

        tokens = [Token(TokenType.NUMBER, 12.4), 
                  Token(TokenType.MULTIPLY), 
                  Token(TokenType.NUMBER, 0.98)]
        
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, MultiplyNode(NumberNode(12.4), NumberNode(0.98)))

        tokens = [Token(TokenType.NUMBER, 12.4), 
                  Token(TokenType.DIVIDE), 
                  Token(TokenType.NUMBER, 0.98)]
        
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, DivideNode(NumberNode(12.4), NumberNode(0.98)))
        
        tokens = [Token(TokenType.NUMBER, 12.4), 
                  Token(TokenType.EXPONENT), 
                  Token(TokenType.NUMBER, 0.98)]
        
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, ExponentNode(NumberNode(12.4), NumberNode(0.98)))

        tokens = [Token(TokenType.NUMBER, 12.4), 
                  Token(TokenType.MODULO), 
                  Token(TokenType.NUMBER, 0.98)]
        
        nodes = Parser(tokens).parse()
        self.assertEqual(nodes, ModuloNode(NumberNode(12.4), NumberNode(0.98)))


    def test_full_expression(self):
        """Test full expression"""

        # 12 + 2^(8/4) - 5 * (7%4)
        tokens = [Token(TokenType.NUMBER, 12),
                  Token(TokenType.PLUS),
                  Token(TokenType.NUMBER, 2),
                  Token(TokenType.EXPONENT),
                  Token(TokenType.LPAREN),
                  Token(TokenType.NUMBER, 8),
                  Token(TokenType.DIVIDE),
                  Token(TokenType.NUMBER, 4),
                  Token(TokenType.RPAREN),
                  Token(TokenType.MINUS),
                  Token(TokenType.NUMBER, 5),
                  Token(TokenType.MULTIPLY),
                  Token(TokenType.LPAREN),
                  Token(TokenType.NUMBER, 7),
                  Token(TokenType.MODULO),
                  Token(TokenType.NUMBER, 4),
                  Token(TokenType.RPAREN)]
                  #Token(TokenType.NUMBER, 3)]
        nodes = Parser(tokens).parse()
        answer = SubtractNode(
            AddNode(
                NumberNode(12),
                ExponentNode(
                    NumberNode(2),
                    DivideNode(
                        NumberNode(8),
                        NumberNode(4)
                    )
                )
            ),
            MultiplyNode(
                NumberNode(5),
                ModuloNode(
                    NumberNode(7),
                    NumberNode(4)
                )
            )
        )
        self.assertEqual(nodes, answer)


if __name__ == '__main__':
    unittest.main()
