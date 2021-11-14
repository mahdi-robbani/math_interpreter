from components.lexer import Lexer
from components.parser_ import Parser
from components.interpreter import Interpreter

while True:
    try:
        text = input("calc >")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        print(tree)
        # If user doesn't type in anything
        if not tree:
            continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        # Instead of crashing the program, just report the exception
        print(e)
