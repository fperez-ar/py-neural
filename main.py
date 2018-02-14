#encoding utf-8
import net_serializer
import networks as sm
import training_set as training

def round_list(float_list, digits=4):
    msg = ""
    for el in float_list:
        msg += str( round(el, digits) ) + ', '

    return msg[:-2]

neuron_layout = [ 5, 10, 5 ]
net = sm.Tanh_network(neuron_layout)
set_1 = training.Training_set( [1,0,0,0,0], [-1,0,0,0,0], 10000)
#set_2 = training.Training_set( [0,0,0,0,1], [0,0,0,0,1], 1000)
#set_3 = training.Training_set( [0,0,1,0,0], [0,0,1,0,0], 1000)

training_collection = (set_1,)

for t_set in training_collection:
    print("Target input\t\t", t_set.input )
    print("Target output\t\t", t_set.output)

    pre = net.get_values(t_set.input)
    net.train( t_set )
    post = net.get_values(t_set.input)

    print("pre-training results\t",  pre) #round_list(pre , 8))
    print("post-training results\t", post)#round_list(post, 8))

    #index = training_collection.index(t_set)
    #name = "config"+str(index)
    #net_serializer.save( net, name )

#for t_set in training_collection:
#    print("target input>\t\t", t_set.input )
#    print("target output>\t\t", t_set.output)
#    print("\t\t",net.get_values(t_set.input))
#net = None
#net = net_serializer.load(name)
