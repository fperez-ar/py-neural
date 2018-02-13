class Connection:
    def __init__(self, ingoing, outgoing, connection_weight):
        #neurons
        self.in_neuron = ingoing
        self.out_neuron = outgoing
        self.weight = connection_weight
