s = "SELECT a, b FROM table WHERE a > 5 ORDER BY b"

class SQL(Transducer):
	def __init__(self, s):
		Transducer.__init__(self, s, 'select')
		self.output = {
			'select': [],
			'from': [],
			'where': [],
			'order': [],
		}

	def state_select(self, token):
		if token == "FROM":
			self.transition('from')
		elif token == "SELECT":
			pass
		else:
			self.output['select'].append(token)

	def state_from(self, token):
		if token == "ORDER":
			self.transition('order')
		elif token == "WHERE":
			self.transition('where')
		else:
			self.output['from'].append(token)

	def state_where(self, token):
		if token == "ORDER":
			self.transition('order')
		else:
			self.output['where'].append(token)

	def state_order(self, token):
		if token == 'BY':
			pass
		else:
			self.output['order'].append(token)

sw = SQL(s.split())
print sw.run()
