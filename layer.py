import neuron

class Layer:

    def connect_layer(self, other_layer):
        for own_neuron in self.neurons:
            for other_neuron in other_layer.neurons:
                own_neuron.connect(other_neuron)

    #sets the one value for all neurones
    def set_value(self, value):
        for own_neuron in self.neurons:
            own_neuron.current_value = value

    # uses array of values for corresponding neurons
    def set_values(self, values):
        if len(self.neurons) != len(values):
            print("ERROR, values and neurons count do not match.")
            return

        for i in range( len(self.neurons) ):
            self.neurons[i].current = values[i]

    def set_target_values(self, values):
        if len(self.neurons) != len(values):
            print("ERROR, values and neurons count do not match.")
            return

        for i in range( len(self.neurons) ):
            self.neurons[i].set_target_value( value[i] )

    def process_value(self):
        for neuron in self.neurons:
            neuron.process_value()

    def process_error(self):
        for neuron in self.neurons:
            neuron.process_error()

    def train(self):
        for neuron in self.neurons:
            neuron.train()

class Layer_sigmoid(Layer):
    def __init__(self, quantity_neurons):
        self.neurons = [ neuron.Neuron_sigmoid() for n in range(quantity_neurons) ]

class Layer_tanh(Layer):
    def __init__(self, quantity_neurons):
        self.neurons = [ neuron.Neuron_tanh() for n in range(quantity_neurons) ]
