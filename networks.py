#encoding utf-8
import layer

class base_network:

    def __get_input_layer(self):
        return self.layers[0]

    def __get_output_layer(self):
        l_index = len(self.layers) - 1
        return self.layers[ l_index ]

    def process_error(self):
        for layer in self.layers:
            layer.process_error()

    def process_value(self):
        for layer in self.layers:
            layer.process_value()

    def set_target_values(self, target_values, layer_index):
        layer = self.layers[layer_index]
        if len(layer.neurons) != len(target_values):
            print("ERROR, values and layer neurons count do not match.")
            return

        neurons = layer.neurons
        for i in range( len(neurons) ):
            neurons[i].set_target_value( target_values[i] )

    def get_values(self, input_values):
        input_layer = self.__get_input_layer()
        if len(input_values) != len( input_layer.neurons):
            print("ERROR, input values and layer neurons count do not match.")
            return

        input_layer.set_values(input_values)
        self.process_value()

        output_layer = self.__get_output_layer()
        output_data = []
        for neuron in output_layer.neurons:
            output_data.append( neuron.current_value )

        return output_data

    def get_errors(self):
        layer_list = []
        for layer in self.layers:
            neuron_error = []
            for neuron in layer.neurons:
                neuron_error.append( neuron.error )
            layer_list.append( neuron_error )
        return layer_list

    def train(self, target_input_values, target_output_values):

        l_index = len (self.layers) - 1
        print(target_input_values)
        print(target_output_values)
        self.set_target_values(target_output_values, l_index)
        self.get_values(target_input_values)
        self.process_error()
        for layer in self.layers:
            layer.train()

    def train(self, training_set):
        l_index = len (self.layers) - 1

        q_training = training_set.training_iterations
        training_iter = 0
        while training_iter < q_training:
            training_iter += 1

            self.set_target_values(training_set.output, l_index)
            self.get_values(training_set.input)
            self.process_error()
            for layer in self.layers:
                layer.train()

    def force_feed(self, layers):
        self.layers = layers
        q_layers = len(self.layers)
        for j in range ( q_layers - 1 ):
            cur_layer  = self.layers[j]
            next_layer = self.layers[j + 1]
            cur_layer.connect_layer(next_layer)

class Sigmoid_network(base_network):

    #receives a list of ints
    def __init__(self, quantity_neurons_layer):
        self.layers = []

        q_layers = len(quantity_neurons_layer)
        for i in range ( q_layers ):
            q_neurons = quantity_neurons_layer[i]
            #create the layers with their appropiate size
            self.layers.append( layer.Layer_sigmoid(q_neurons) )

        for j in range ( q_layers - 1 ):
            cur_layer  = self.layers[j]
            next_layer = self.layers[j + 1]
            cur_layer.connect_layer(next_layer)



class Tanh_network(base_network):
    #receives a list of ints
    def __init__(self, quantity_neurons_layer):
        self.layers = []

        q_layers = len(quantity_neurons_layer)
        for i in range ( q_layers ):
            q_neurons = quantity_neurons_layer[i]
            #create the layers with their appropiate size
            self.layers.append( layer.Layer_tanh(q_neurons) )

        for j in range ( q_layers - 1 ):
            cur_layer  = self.layers[j]
            next_layer = self.layers[j + 1]
            cur_layer.connect_layer(next_layer)
