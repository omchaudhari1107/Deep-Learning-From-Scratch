# a single neuron contain (weighted sum+step function)
import numpy as np

inputs = [-1.2,-5.1,-2.1]
weights = [-1,-2,3]

def weighted_sum(input,weight):
    sum=0
    for i,w in zip(input,weight):
        sum+=i*w
    return sum
def step_function(sum):
    return np.maximum(0,sum)

def neuron(inputs,weights):
    sum=weighted_sum(inputs,weights)
    output = step_function(sum)
    return output

print(neuron(inputs,weights))