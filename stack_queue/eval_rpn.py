"""
LeetCode 150

Evaluate the value of an arithmetic expression in Reverse 
Polish Notation.

Valid operators are +, -, *, /. Each operand may be an 
integer or another expression.

Note:
    - Division between two integers should truncate toward zero.
    - The given RPN expression is always valid. That means the 
      expression would always evaluate to a result and there won't 
      be any divide by zero operation.
"""

def eval_rpn(tokens):
    def _add(x, y):
        return x+y

    def _sub(x, y):
        return x-y

    def _mul(x, y):
        return x*y

    def _div(x, y):
        return int(float(x)/float(y))
    
    mapper = {
        '+': _add, 
        '-': _sub, 
        '*': _mul, 
        '/': _div
        }
    stack = []
    for ele in tokens:
        if ele not in mapper:
            stack.append(int(ele))
        else:
            e1 = stack.pop()
            e2 = stack.pop()
            stack.append(mapper[ele](e2, e1))
    return stack.pop()

def test_eval_rpn():
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22