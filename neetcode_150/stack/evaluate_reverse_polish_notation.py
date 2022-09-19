from operator import add, sub, truediv, mul

VALID_OPS = ['+', '-', '*', '/']


def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if is_num(token):
            stack.append(token)
        elif is_operator(token):
            operand2 = stack.pop()
            operand1 = stack.pop()
            res = perform_operation(
                float(operand1),
                float(operand2),
                token
            )
            stack.append(res)

    return stack[0]


def perform_operation(operand1, operand2, operator):
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    return int(operators[operator](operand1, operand2))


def is_operator(operator):
    if operator in VALID_OPS:
        return True
    return False


def is_num(num):
    try:
        float(num)
        return True
    except:
        return False


if __name__ == '__main__':
    tokens1 = ["2", "1", "+", "3", "*"]  # Output: 9
    tokens2 = ["4", "13", "5", "/", "+"]  # Output: 6
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]  # Output: 22

    assert eval_rpn(tokens1) == 9
    assert eval_rpn(tokens2) == 6
    assert eval_rpn(tokens3) == 22


'''
["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
exp = "9+3" = 12

["10", "6", "12", "-11", "*", "/", "*", "17", "+", "5", "+"]
exp = "12*-11" = -132

["10", "6", "-132", "/", "*", "17", "+", "5", "+"]
exp = 6/-132 = -0.04545454545

["10", "-0.04545454545", "*", "17", "+", "5", "+"]
exp = 10*-0.04545454545 = -0.45454545454

[-0.45454545454, "17", "+", "5", "+"]
exp = -0.45454545454+17 = 16.5454545455

[16.5454545455, "5", "+"]
exp = 16.5454545455+5 = 21.5454545455
'''
