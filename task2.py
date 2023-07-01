result = None
operand = None
operator = None

def operand_value(operand1):
    while operand1 is not float:
        try:
            operand1 = float(operand1)
            return operand1
        except ValueError:
            print(f"{operand1} is not a number. Try again.")
            return False

def operator_value(operator1):
    try:
        if operator1 != "+" and operator1 != "-" and operator1 != "*" and operator1 != "/":
            print(f"{operator1} is not '+' or '-' or '/' or '*'. Try again.")
            return False
        else:
            return operator1
    except TypeError:
        print(f"{operator1} is not '+' or '-' or '/' or '*'. Try again.")
        return False


result = input()
while operand_value(result) is False:
    result = input()
result = operand_value(result)

operator = input()
while operator_value(operator) is False:
    operator = input()
operator = operator_value(operator)

while True:
    operand = input()
    while operand_value(operand) is False:
        operand = input()
    operand = operand_value(operand)

    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    else:
        result /= operand

    operator = input()
    if ord(operator) == 61:
        print(result)
        break
    else:
        while operator_value(operator) is False:
            operator = input()
        operator = operator_value(operator)

