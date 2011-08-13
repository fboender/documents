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
