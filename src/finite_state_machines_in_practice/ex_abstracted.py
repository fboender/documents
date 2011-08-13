class TransducerError(Exception):
    pass

class Transducer(object):
    def __init__(self, input, start_state):
        self.input = input
        self.output = []
        self.cur_state = start_state

    def run(self):
        for symbol in self.input:
            method = getattr(self, 'state_%s' % (self.cur_state), None)
            if not method:
                raise TransducerError('No method handler found for state \'%s\'' % (self.cur_state))
            method(symbol)
        return(self.output)

    def transition(self, new_state):
        handler = getattr(self, 'action_%s_exit' % (self.cur_state), None)
        if handler:
            handler()
        handler = getattr(self, 'action_transition', None)
        if handler:
            handler(self.cur_state, new_state)
        handler = getattr(self, 'action_%s_enter' % (new_state), None)
        if handler:
            handler()
        self.cur_state = new_state
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
