from transitions import Machine
from transitions import State
from .state_decorator import states
from graphviz import Digraph

states.append(State(name="start"))


class Starter(object):

    def __init__(self):
        self.store = {}
        self._get_token()
        self.machine = Machine(model=self, states=states, transitions=self.STATE_FLOW, initial='start')

    def start(self):
        getattr(self, self.START_METHOD)()

    def png(self):
        nodes = set([x["source"] for x in self.STATE_FLOW] + [x["dest"] for x in self.STATE_FLOW])
        g = Digraph('STATE_FLOW')
        for node in nodes:
            g.node(name=node, color='blue')
        for transition in self.STATE_FLOW:
            g.edge(transition['source'], transition['dest'], color='black', label=transition['trigger'])

        g.render('state_flow', format='png', view=True)
