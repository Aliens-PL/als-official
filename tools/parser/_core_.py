__import__('sys').path.append('..') # Get rid of higher dir msg


class CoreEngine(object):
    
    def __init__(self, _tmp_f):
        self.lexer      = None
        self.parser     = None
        self.eval       = None
        self._f_cache   = None

        self.listener_v = -1
        # Here we start MultiThreading .

    def Listener_(self):
        if self.listener_v == -1:
            # Listen and wait for the sum   (last_step_id)[start_token - end_token]
            pass
        else:
            #done
            pass


    def _clear_steps(self):
        # do our mem cleaning !
        pass

