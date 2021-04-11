class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None
        
class Solution:
    """
    @param: expression: A string array
    @return: The root of expression tree
    """

    def build(self, expression):
        def _exec(op, nodes):
            node = ExpressionTreeNode(op)
            node.right = nodes.pop()
            node.left = nodes.pop()
            nodes.append(node)

        def _exec_all(nodes, ops):
            while ops and ops[-1] != '(':
                _exec(ops.pop(), nodes)

        nodes = []
        ops = []
        op_symbols = ('+', '-', '*', '/', '(')

        for ch in expression:
            if ch in op_symbols:
                if ch in ('+', '-'):
                    _exec_all(nodes, ops)
                ops.append(ch)

            elif ch == ')':
                _exec_all(nodes, ops)
                if ops[-1] == '(':
                    ops.pop()
            else:
                nodes.append(ExpressionTreeNode(ch))
                if ops and ops[-1] in ('*', '/'):
                    _exec(ops.pop(), nodes)

        _exec_all(nodes, ops)

        if nodes:
            return nodes[-1]
