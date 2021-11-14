# Simple Math Interpreter

A math interpreter coded in Python which can evaluate simple math calculations. It can currently perform the following operations:
- Add
- Subtract
- Multiply
- Divide
- Exponent
- Modulo

The program works using the following procedure:
- Converts the user input into tokens using the lexer
- Converts the tokens to a tree using the parser
- Evaluates the tree using the interpreter which return a value

## Lexer

The lexer groups the input characters into small segments called tokens and identifies the type of each token, similarly to how we group letters into words such as nouns and verbs.

The characters in the input `12 + 24` are grouped into the tokens `NUMBER:12`, `PLUS`, and `NUMBER:24`.

Whitespace is ignored by the lexer.

The tokens are then passed on to the parser.

## Parser

The parser analyzes the sequence of tokens to determine what is intended to happen and in what order, similarly to how we make sense of sentences based on the sequence and types of words.

When the parser sees `NUMBER`, followed by `PLUS`, followed by `NUMBER`, it passes on that the two numbers should be added together. In the case of a multiply operation added into the mix, the parser can determine that the two numbers next to the multiply operator should be multiplied first before the addition takes place.

The result, respresented as a tree, is then pased on to the interpreter.

## Interpreter

The interpeter simply does what's intended according to the parser's results, and contains the code for all the different math operations.

The interpeter could be swapped out for a compiler which generates machine-readable code that your computer can later execute, or could be swapped out for a transpiler which generates code for another language.

# Running the Program

Requirements:
 - [Python3](https://www.python.org/downloads/) ^3.9

Run: 
`python src/main.py` 

Unit testing:

`python -m unittest`