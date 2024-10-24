# a single layer
import numpy as np

inputs = [-1.2,-5.1,-2.1,0]

weights1 = [-.2,-.8,-.5,1]
weights2 = [.5,-.91,.26,-.5]
weights3 = [-1,-2,3,4]

bias1=1
bias2=2
bias3=0

def weighted_sum(input,weight,bias):
    sum=0
    for i,w in zip(input,weight):
        sum+=i*w
    return sum+bias
def step_function(sum):
    return np.maximum(0,sum)

def neuron(inputs,weights,bias):
    sum=weighted_sum(inputs,weights,bias)
    output = step_function(sum)
    return output

print(neuron(inputs,weights1,bias1))
print(neuron(inputs,weights2,bias2))
print(neuron(inputs,weights3,bias3))