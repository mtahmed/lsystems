class LSystem(object):
    '''Represents an L-System with intial state, production rules and alphabet.
    '''
    def __init__(self, initial, productions, alphabet=None):
        '''
        :param initial: A string of symbols representing the initial state.
        :param productions: A dictionary from symbol to a string of symbols.
        :param alphabet: A list of alphabet in the language.
        '''
        self.initial = initial
        self.productions = productions
        self.alphabet = alphabet

        self.state = self.initial

        return

    def step(self):
        '''Step once through the LSystem.

        In other words, apply the production rules once to the current state.
        '''
        new_symbols = []
        for symbol in self.state:
            try:
                new_symbol = self.productions[symbol]
                new_symbols.append(new_symbol)
            except KeyError:
                new_symbols.append(symbol)

        self.state = ''.join(new_symbols)

        return

    def step_n(self, n):
        '''Step n times through the LSystem.

        In other words, invoke the step function n times.
        '''
        for _ in range(n):
            self.step()

        return

    def draw(self):
        '''Draw the current state.

        The default is just to print the state string.
        '''
        print(self.state)
