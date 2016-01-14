<a name="nn.Linear"></a>
## Linear ##

```lua
module = nn.Linear(inputDimension, outputDimension)
```

Applies a linear transformation to the incoming data, i.e. `y = Ax + b`. The `input` tensor given in `forward(input)` must be either a vector (1D tensor) or matrix (2D tensor). If the input is a matrix, then each row is assumed to be an input sample of given batch.

You can create a layer in the following way:

```lua
 module = nn.Linear(10, 5)  -- 10 inputs, 5 outputs
```

Usually this would be added to a network of some kind, e.g.:

```lua
 mlp = nn.Sequential()
 mlp:add(module)
```

The weights and biases (_A_ and _b_) can be viewed with:

```lua
 print(module.weight)
 print(module.bias)
```

The gradients for these weights can be seen with:

```lua
 print(module.gradWeight)
 print(module.gradBias)
```

As usual with `nn` modules, applying the linear transformation is performed with:

```lua
x = torch.Tensor(10) -- 10 inputs
y = module:forward(x)
```
