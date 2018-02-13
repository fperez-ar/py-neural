#encoding utf-8
import simple_network as sm
import training_set as training

neuron_layout = [ 5, 10, 5 ]
net = sm.Simple_network(neuron_layout)
set_1 = training.Training_set( [1,0,0,0,0], [1,0,0,0,0], 100 )
set_1 = training.Training_set( [0,0,0,0,1], [0,0,0,0,1], 100 )


training_iter = 0
q_training = 10000

print("pre-training")
print(net.get_values(tgt_input))

while training_iter < q_training:
    net.train( tgt_input, tgt_output )
    training_iter += 1
    #print(net.get_values(tgt_input))


print("post-training")
print(net.get_values(tgt_input))

quit()

done = False
#while not done:

#if input("Continue? Y/N") == 'y':
  #done = True
