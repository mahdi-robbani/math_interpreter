from nodes import *
from values import *


class Interpreter:
    """Takes in a root node of a tree and processes that tree to return
    a number."""

    def visit(self, node):
        """Takes in a node and identifies which method should handle it.
        Each method returns a RealNumber object. Each RealNumber has a
        value that can be extracted.
        """

        method_name = f"visit_{type(node).__name__}" # e.g. visit_AddNode
        method = getattr(self, method_name) # retrieve the appropriate method
        return method(node)

    def visit_NumberNode(self, node):
        return RealNumber(node.value)

    def visit_AddNode(self, node):
        # self.visit results in the creation of a RealNumber object
        # We extract the value from that real number object
        node_a_result = self.visit(node.node_a).value
        node_b_result = self.visit(node.node_b).value 
        return RealNumber(node_a_result + node_b_result)

    def visit_SubtractNode(self, node):
        node_a_result = self.visit(node.node_a).value 
        node_b_result = self.visit(node.node_b).value 
        return RealNumber(node_a_result - node_b_result)

    def visit_MultiplyNode(self, node):
        node_a_result = self.visit(node.node_a).value 
        node_b_result = self.visit(node.node_b).value 
        return RealNumber(node_a_result * node_b_result)

    def visit_DivideNode(self, node):
        try:
            node_a_result = self.visit(node.node_a).value 
            node_b_result = self.visit(node.node_b).value 
            return RealNumber(node_a_result / node_b_result)
        except:
            raise Exception("Runtime math error")
    
    def visit_PlusNode(self, node):
        return self.visit(node.node) 

    def visit_MinusNode(self, node):
        return RealNumber(-self.visit(node.node).value)

    def visit_PowerNode(self, node):
        node_a_result = self.visit(node.node_a).value 
        node_b_result = self.visit(node.node_b).value 
        return RealNumber(node_a_result ** node_b_result)
