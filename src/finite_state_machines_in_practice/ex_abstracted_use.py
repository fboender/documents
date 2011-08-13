s = "ls -la 'My Documents' /home /etc"

CHAR_QUOTE = "'"
CHAR_SPACE = " "

class Splitwords(Transducer):
	def __init__(self, s):
		Transducer.__init__(self, s, 'unquoted')
		self.output.append('')

	def state_unquoted(self, c):
		if c == CHAR_QUOTE:
			self.transition('quoted')
		elif c == CHAR_SPACE:
			self.append_word()
		else:
			self.append_char(c)

	def state_quoted(self, c):
		if c == CHAR_QUOTE:
			self.transition('unquoted')
		else:
			self.append_char(c)

	def append_word(self):
		if self.output[-1]:
			self.output.append('')

	def append_char(self, c):
		self.output[-1] += c

sw = Splitwords(s)
print sw.run()
