#encoding utf-8
import net_serializer
import simple_network as sm
import training_set as training

def round_list(float_list):
    msg = ""
    for el in float_list:
        msg += str( round(el, 4) ) + ', '

    return msg[:-2]

neuron_layout = [ 5, 10, 5 ]
net = sm.Simple_network(neuron_layout)
set_1 = training.Training_set( [1,0,0,0,0], [1,0,0,0,0], 1000)
set_2 = training.Training_set( [0,0,0,0,1], [0,0,0,0,1], 1000)
set_3 = training.Training_set( [0,0,1,0,0], [0,0,1,0,0], 1000)

training_collection = (set_1, set_2, set_3)

for t_set in training_collection:
    print("Target input\t\t", t_set.input )
    print("Target output\t\t", t_set.output)

    pre = net.get_values(t_set.input)
    net.train( t_set )
    post = net.get_values(t_set.input)

    print("pre-training results\t",  round_list(pre))
    print("post-training results\t", round_list(post))
    index = training_collection.index(t_set)
    name = "config"+str(index)
    net_serializer.save( net, name )

#for t_set in training_collection:
#    print("target input>\t\t", t_set.input )
#    print("target output>\t\t", t_set.output)
#    print("\t\t",net.get_values(t_set.input))

net = None
net = net_serializer.load(name)


for t_set in training_collection:
    print("target input>", t_set.input )
    print("target output>", t_set.output)
    print(net.get_values(t_set.input))
