import shlex

s = '2 * 3 + 2 / 3'

stack = [2.0, 3.0, '*', 2.0, 3.0, '/', '+']


# Postfix evaluator
op_fn = {
	'*'  : (2, lambda x, y: x*y),
	'/'  : (2, lambda x, y: x/y),
	'+'  : (2, lambda x, y: x+y),
	'-'  : (2, lambda x, y: x-y),
	'mod': (2, lambda x, y: x%y),
	'%'  : (2, lambda x, y: x%y),
	'^'  : (2, lambda x, y: x**y),
}

stack_out = []
for token in stack:
	if token in op_fn:
		args_nr, func = op_fn[token]
		args = []
		for i in range(-args_nr, 0):
			args.append(stack_out.pop(i))
		stack_out.append(func(*args))
	else:
		stack_out.append(token)

print stack_out
