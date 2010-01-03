import shlex
import math

class CalcError(Exception):
  pass

class Calc(object):

  operator_rassoc = ['^']
  operator_prec = {
    '('   : 0,
    ')'   : 0,
    '<<'  : 1,
    '>>'  : 1,
    '+'   : 2,
    '-'   : 2,
    '*'   : 3,
    '/'   : 3,
    '^'   : 4,
    '%'   : 4,
    'mod' : 4,
    'log' : 4,
  }
  constants = {
    'pi' : math.pi,
    'e'  : math.e,
  }
  functions = [
    'sqrt', 'floor', 'ceil',
  ]
  op_fn = {
    '*'    : (2, lambda x, y: x*y),
    '/'    : (2, lambda x, y: x/y),
    '+'    : (2, lambda x, y: x+y),
    '-'    : (2, lambda x, y: x-y),
    'mod'  : (2, lambda x, y: x%y),
    'log'  : (1, lambda x: math.log10(x)),
    '%'    : (2, lambda x, y: x%y),
    '^'    : (2, lambda x, y: x**y),
    '<<'   : (2, lambda x, y: int(x)<<int(y)),
    '>>'   : (2, lambda x, y: int(x)>>int(y)),
    'sqrt' : (1, math.sqrt),
    'floor': (1, math.floor),
    'ceil' : (1, math.ceil),
  }

  def __init__(self):
    pass

  def eval(self, expression):
    expression = expression.strip()
    return(self.rpn_eval(self.infix_to_rpn(expression)))

  def infix_to_rpn(self, s):
    lex = shlex.shlex(s)
    lex.wordchars += '.<>'
    stack_out = []
    stack_op = []
    
    token = True
    while token:
      prev_token = token
      token = lex.get_token()

      if token == '-' and (prev_token == True or prev_token in self.operator_prec):
        # We're dealing with a negative number
        token += lex.get_token()

      if token == '*':
        # Special case for '**' which is the power operator.
        peek_token = lex.get_token()
        if peek_token == '*':
          token = '^'
        else:
          lex.push_token(peek_token)

      if token:
        if token in self.constants:
          stack_out.append(self.constants[token])
        elif token in self.functions:
          stack_op.append(token)
        elif token == ',':
          while stack_op and stack_op[-1] != '(':
            stack_out.append(stack_op.pop())
        elif token == '(':
          stack_op.append(token)
        elif token == ')':
          while stack_op and stack_op[-1] != '(':
            stack_out.append(stack_op.pop())
          if not stack_op:
            raise CalcError('Unmatched parenthesis.')
          stack_op.pop()
        elif token in self.operator_prec:
          # Operator
          while \
            stack_op and ( \
              stack_op[-1] not in self.operator_prec or \
              ( \
                (token not in self.operator_rassoc and self.operator_prec[token] <= self.operator_prec[stack_op[-1]]) or \
                (token in self.operator_rassoc and self.operator_prec[token] < self.operator_prec[stack_op[-1]]) \
              )
            ):
            stack_out.append(stack_op.pop())
          stack_op.append(token)
        else:
          # Operand
          try:
            stack_out.append(float(token))
          except ValueError, e:
            raise CalcError('Illegal operand \'%s\'.' % (token))

    if '(' in stack_op or ')' in stack_op:
      raise CalcError('Unmatched parenthesis.')

    stack_op.reverse()
    stack_out += stack_op

    return(stack_out)
      
  def rpn_eval(self, stack):
    try:
      stack_out = []
      for token in stack:
        if token in self.op_fn:
          args_nr, func = self.op_fn[token]
          args = []
          try:
            for i in range(-args_nr, 0):
              args.append(stack_out.pop(i))
          except IndexError, e:
            raise CalcError('Insufficient operands for "%s" operator.' % (token))
          try:
            stack_out.append(func(*args))
          except Exception, e:
            raise CalcError(e.message)
        else:
          stack_out.append(token)
        prev_token = token

      if stack_out:
        return(stack_out[0])
      else:
        return('I cant make sense of it at all.')
    except OverflowError, err:
      return('Overflow.')

c = Calc()
print "Enter an equation. 'quit' to quit."
l = ''
while l.lower() != 'quit':
  l = raw_input('> ')
  try:
    print c.eval(l)
  except CalcError, e:
    print "Error: %s" % (e.message)
