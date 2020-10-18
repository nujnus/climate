from transitions import Machine
from transitions import State
from .state_decorator import states

states.append(State(name="start"))

class Starter(object):

  def __init__(self):
    self.store = {}
    self._get_token()
    self.machine = Machine(model=self, states=states, transitions=self.STATE_FLOW, initial='start')


  def start(self):
    getattr(self, self.START_METHOD)()
