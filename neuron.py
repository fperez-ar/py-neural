import math
import random as rng
import connection


class Neuron:

    def __init__(self):
        #lists of connections
        self.in_connections = []
        self.out_connections = []

        self.error = 0
        self.current_value = 0
        self.target_value = 0


    def connect(self, out):
        in_neuron = self
        out_neuron = out
        new_conn = connection.Connection(in_neuron, out_neuron, rng.random() )
        #add an outgoing connection from self, to other neuron
        self.out_connections.append(new_conn)

        #add an incoming connection from other to self
        out.in_connections.append(new_conn)


    def set_target_value(self, value):
        self.target_value = value;


    def process_value(self):
        sum = 0

        if not self.in_connections: #empty list
            #no incoming connections means it's from the input layer
            pass

        for curr_connection in self.in_connections:
            sum += curr_connection.in_neuron.current_value * curr_connection.weight

        self.current_value = 1 / ( 1 + pow(math.e, -sum) )


    def process_error(self):
        #input layer
        if not self.in_connections: #empty list
            return

        #output layer
        if not self.out_connections: #empty list
            self.error = (self.target_value - self.current_value) * self.current_value * (1 - self.current_value)
            return

        #hidden layer
		#error oculta = x * Valor * (1 - Valor)
		#  x = suma( errores con_salida * peso con_salida)
        sum = 0

        for curr_connection in self.out_connections:
            sum += curr_connection.out_neuron.error * curr_connection.weight

        self.error = sum * self.current_value * (1 - self.current_value)


    def train(self):
        for curr_connection in self.out_connections:
            curr_connection.weight += self.current_value * curr_connection.out_neuron.error
