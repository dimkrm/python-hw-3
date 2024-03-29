import sys
if len(sys.argv) != 4 or 2:
    print('Arg len should be 4 or 2')
    sys.exit()
left_operand = sys.argv[1 or 0]
right_operand = sys.argv[3 or 2]
operation = sys.argv[2 or 1]
allowed_operations = ['+', '-', '/', '*', '%']
if operation not in allowed_operations:
    print('Operation is not allowed')
    sys.exit()
try:
    left_operand = int(left_operand)
    right_operand = int(right_operand)
except ValueError:
    print('Left and Right operands must be int')
    sys.exit()
if operation == '/' and right_operand == 0:
    print('Division by zero is not allowed')
    sys.exit()
print(eval(f'{left_operand}{operation}{right_operand}'))
'100/1'.split('/') # operation = /, left, right = ['100', '1']
'100+1'.split('+') # ['100', '1'] 