import simple_network as sm
import neuron, layer, pickle

def save(simple_net, name = "config"):
    with open(name, 'wb') as config_file:
        print("writing", name)
        pickle.dump(simple_net, config_file)

def load(name):
    with open(name, 'rb') as config_file:
        print("loading", name)
        return pickle.load(config_file)


# def save(simple_net, name = "config"):
#     config_file = open(name, 'w+')
#     for layer in simple_net.layers:
#         config_file.write( "layer\n" )
#         for neuron in layer.neurons:
#             config_file.write( str(neuron) + '\n' )

# def load(name):
#     config_file = open(name, 'r')
#     current_layer = None
#     layers = []
#     lines = config_file.readlines()
#
#     for line in lines:
#         if line.find("layer") >= 0:
#             current_layer = layer.Layer(0)
#         else:
#             neuron_elements = line.split(', ')
#             new_neuron = neuron.Neuron()
#             new_neuron.error         = float( neuron_elements[0] )
#             new_neuron.current_value = float( neuron_elements[1] )
#             new_neuron.target_value  = float( neuron_elements[2] )
#             current_layer.neurons.append( new_neuron )
#
#         layers.append( current_layer )
#     #how to serialize connections??
#     return layers
