from abc import ABC, abstractmethod

class Context():

    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def call_strategy(self, data):
        result = self._strategy.do_algorithm(data)
        print(",".join(str (el) for el in result))

class Strategy(ABC):

    @abstractmethod
    def do_algorithm(self, data):
        pass

class reverse_strategy(Strategy):

    def do_algorithm(self, data):
        return reversed(sorted(data))

class sort_strategy(Strategy):

    def do_algorithm(self, data):
        return sorted(data)

if __name__ == "__main__":

    data = [29,6,78,35,70,89,23,56,0]

    print("Client: Strategy set to normal sorting")
    context = Context(sort_strategy())
    context.call_strategy(data)
    print("")


    print("Client: Strategy set to reverse sorting")
    context = Context(reverse_strategy())
    context.call_strategy(data)
