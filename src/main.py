from components.lexer import Lexer
from components.parser_ import Parser
from components.interpreter import Interpreter

if __name__ == "__main__":
    print("Press 'q' to quit.")
    while True:
        try:
            text = input("calc >")
            # check if user wants to quit
            if text == "q":
                print("Exiting...")
                break
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
