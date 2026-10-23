inputs = [4.3, 5.1, 6.7, 3.9, 2.8]

weights = [[0.2, 0.5, 0.3, 0.1, 0.4],
           [0.5, -0.9, 0.3, -0.1, 0.6],
           [0.3, -0.4, 0.7, 0.3, 0.8]]

biases = [2, 3, 0.5]


layer_outputs = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)


