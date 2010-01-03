import shlex

s = '2 * (3 + 5) + 1'

operator_prec = {
	'('   : 0,
	')'   : 0,
	'+'   : 1,
	'-'   : 1,
	'*'   : 2,
	'/'   : 2,
	'^'   : 3,
	'%'   : 3,
}

lex = shlex.shlex(s)
lex.wordchars += '.'
stack_out = []
stack_op = []
	
# Read tokens from input string
for token in lex:
	# Parenthesis
	if token == '(':
		stack_op.append(token)
	elif token == ')':
		# Pop operands from the operator stack to the output until we find a
		# matching '('
		while stack_op and stack_op[-1] != '(':
			stack_out.append(stack_op.pop())
		if not stack_op:
			raise CalcError('Unmatched parenthesis')
		# Pop the '(' from the stack and discard it
		stack_op.pop()
	# If the token is an operator...
	elif token in operator_prec:
		# Pop operators from the operator stack as long as our token has a
		# lower or equal precedence to the operator at the top of the stack.
		while stack_op and operator_prec[token] <= operator_prec[stack_op[-1]]:
			stack_out.append(stack_op.pop())
		# Add the token to the operator stack
		stack_op.append(token)
	# If token isn't an operator, we assume it's a operand...
	else:
		stack_out.append(float(token))

# Done with the tokens in the input string. Now pop all the operators left
# on the operator stack to the output stack. This is the same as reversing
# the operator stack and appending it to the output, so we do that.
stack_op.reverse()
stack_out += stack_op

print stack_out

