import unittest
from src.components.types.tokens import TokenType, Token
from src.components.lexer import Lexer

class TestLexer(unittest.TestCase):
    """Contains all the tests for the Lexer class"""

    def test_empty(self):
        """Ensure an empty string results in no tokens"""

        tokens = list(Lexer("").generate_tokens())
        self.assertEqual(tokens, [])

    def test_whitespace(self):
        """Ensure white space results in no tokens"""

        tokens = list(Lexer(" \n\t \t\n\n\t\t\n ").generate_tokens())
        self.assertEqual(tokens, [])

    def test_number(self):
        """Ensure numbers return corrent number token"""

        tokens = list(Lexer("123 123.456 .456 .123 .").generate_tokens())
        answer = [Token(TokenType.NUMBER, 123),
                  Token(TokenType.NUMBER, 123.456),
                  Token(TokenType.NUMBER, 0.456),
                  Token(TokenType.NUMBER, 0.123),
                  Token(TokenType.NUMBER, 0.0)]
        self.assertEqual(tokens, answer)

    def test_operator(self):
        """Ensure operators return corrent operator token"""

        tokens = list(Lexer("+-*/^").generate_tokens())
        answer = [Token(TokenType.PLUS),
                  Token(TokenType.MINUS),
                  Token(TokenType.MULTIPLY),
                  Token(TokenType.DIVIDE),
                  Token(TokenType.POWER)]
        self.assertEqual(tokens, answer)

    def test_parens(self):
        """Ensure parentheses return corrent parentheses token"""

        tokens = list(Lexer("()").generate_tokens())
        answer = [Token(TokenType.LPAREN),
                  Token(TokenType.RPAREN)]
        self.assertEqual(tokens, answer)

    def test_all(self):
        """Test all token types"""

        tokens = list(Lexer("12 + 2^(8/4) - 5 * 3").generate_tokens())
        answer = [Token(TokenType.NUMBER, 12),
                  Token(TokenType.PLUS),
                  Token(TokenType.NUMBER, 2),
                  Token(TokenType.POWER),
                  Token(TokenType.LPAREN),
                  Token(TokenType.NUMBER, 8),
                  Token(TokenType.DIVIDE),
                  Token(TokenType.NUMBER, 4),
                  Token(TokenType.RPAREN),
                  Token(TokenType.MINUS),
                  Token(TokenType.NUMBER, 5),
                  Token(TokenType.MULTIPLY),
                  Token(TokenType.NUMBER, 3)]
        self.assertEqual(tokens, answer)

if __name__ == '__main__':
    unittest.main()
