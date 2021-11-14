import unittest
from src.components.types.nodes import *
from src.components.interpreter import Interpreter
from src.components.types.values import RealNumber

class TestInterpreter(unittest.TestCase):
    """Contains all the tests for the Interpreter class"""

    def test_numbers(self):
        value = Interpreter().visit(NumberNode(12.1))
        self.assertEqual(value, RealNumber(12.1))

    def test_individual_operations(self):
        value = Interpreter().visit(AddNode(NumberNode(3), NumberNode(7)))
        self.assertEqual(value, RealNumber(10))

        value = Interpreter().visit(SubtractNode(NumberNode(3), NumberNode(7)))
        self.assertEqual(value, RealNumber(-4))

        value = Interpreter().visit(MultiplyNode(NumberNode(3), NumberNode(7)))
        self.assertEqual(value, RealNumber(21))

        value = Interpreter().visit(DivideNode(NumberNode(3), NumberNode(7)))
        self.assertAlmostEqual(value.value, 0.42857, 5)

        value = Interpreter().visit(ExponentNode(NumberNode(3), NumberNode(7)))
        self.assertEqual(value, RealNumber(2187))

        value = Interpreter().visit(ModuloNode(NumberNode(3), NumberNode(7)))
        self.assertEqual(value, RealNumber(3))

        # Ensure code raises exception
        with self.assertRaises(Exception):
            # Divide by zero
            Interpreter.visit(DivideNode(NumberNode(1), NumberNode(0)))

        with self.assertRaises(Exception):
            # Divide by zero
            Interpreter.visit(ModuloNode(NumberNode(1), NumberNode(0)))

    def test_full_expression(self):
        tree = SubtractNode(
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
                #NumberNode(3)
            )
        )
        result = Interpreter().visit(tree)
        self.assertAlmostEqual(result.value, 1.0, 5)

if __name__ == '__main__':
    unittest.main()
