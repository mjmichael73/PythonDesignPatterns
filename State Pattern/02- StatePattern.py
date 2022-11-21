import unittest

class State(object):
    pass

class ConcreteState1(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
    
    def switch_state(self):
        self.state_machine.state = self.state_machine.state2

class ConcreteState2(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
    
    def switch_state(self):
        self.state_machine.state = self.state_machine.state1

class StateMachine(object):
    def __init__(self):
        self.state1 = ConcreteState1(self)
        self.state2 = ConcreteState2(self)
        self.state = self.state1
    
    def switch(self):
        self.state.switch_state()
    
    def __str__(self):
        return str(self.state)

def main():
    state_machine = StateMachine()
    print(state_machine)
    state_machine.switch()
    print(state_machine)


class GenericStatePatternTest(unittest.TestCase):
    def setUp(self):
        self.state_machine = StateMachine()
    
    def tearDown(self):
        pass

    def test_state_machine_initializes_correctly(self):
        self.assertIsInstance(self.state_machine.state, ConcreteState1)
    
    def test_switch_from_state_1_to_state_2(self):
        self.state_machine.switch()
        self.assertIsInstance(self.state_machine.state, ConcreteState2)
    
    def test_switch_from_state_2_to_state_1(self):
        self.state_machine.switch()
        self.state_machine.switch()
        self.assertIsInstance(self.state_machine.state, ConcreteState1)


if __name__ == "__main__":
    unittest.main()