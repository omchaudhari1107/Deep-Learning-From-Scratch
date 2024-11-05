
inputs = [-1.2,-5.1,-2.1,0]
weights = [[-.2,-.8,-.5,1], [.5,-.91,.26,-.5],[-1,-2,3,4]]
biases = [2,3,.5]

layer_outputs=[]
for n_weight, n_bias in zip(weights,biases):
    n_output=0
    for input,weights in zip(inputs,n_weight):
        n_output+=input*weights # x1*w1 where w1=[multiples]
    n_output+=n_bias
    layer_outputs.append(n_output)
print(layer_outputs)

# tensor : am object that can be represent as an array..
import numpy as np

a=[1,2,3]
b=[2,3,4]
print(np.dot(a,b))


# 1*2+2*3+3*4 = 20
input = [-1.2,-5.1,-2.1,0]
weights = [-.2,-.8,-.5,1]
bias = 2
output = np.dot(input,weights)+bias
print(output)


# dot product of an layer
inputs = [-1.2,-5.1,-2.1]
weights = [
    [-0.2, -0.8, -0.5],
    [0.5, -0.91, 0.26],
    [-1, -2, 3]
]
biases = [2,3,.5]
output = np.dot(weights,inputs)+biases
print(output)
