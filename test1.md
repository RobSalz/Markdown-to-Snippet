<a name="nn.SpatialConvolution"></a>
### SpatialConvolution ###

```lua
module = nn.SpatialConvolution(nInputPlane, nOutputPlane, kW, kH, [dW], [dH], [padW], [padH])
```

Applies a 2D convolution over an input image composed of several input planes. The `input` tensor in
`forward(input)` is expected to be a 3D tensor (`nInputPlane x height x width`).

The parameters are the following:
* `nInputPlane`: The number of expected input planes in the image given into `forward()`.
* `nOutputPlane`: The number of output planes the convolution layer will produce.
* `kW`: The kernel width of the convolution
* `kH`: The kernel height of the convolution
* `dW`: The step of the convolution in the width dimension. Default is `1`.
* `dH`: The step of the convolution in the height dimension. Default is `1`.
* `padW`: The additional zeros added per width to the input planes. Default is `0`, a good number is `(kW-1)/2`.
* `padH`: The additional zeros added per height to the input planes. Default is `padW`, a good number is `(kH-1)/2`.

Note that depending of the size of your kernel, several (of the last)
columns or rows of the input image might be lost. It is up to the user to
add proper padding in images.

If the input image is a 3D tensor `nInputPlane x height x width`, the output image size
will be `nOutputPlane x oheight x owidth` where
```lua
owidth  = floor((width  + 2*padW - kW) / dW + 1)
oheight = floor((height + 2*padH - kH) / dH + 1)
```

The parameters of the convolution can be found in `self.weight` (Tensor of
size `nOutputPlane x nInputPlane x kH x kW`) and `self.bias` (Tensor of
size `nOutputPlane`). The corresponding gradients can be found in
`self.gradWeight` and `self.gradBias`.

The output value of the layer can be precisely described as:
```lua
output[i][j][k] = bias[k]
+ sum_l sum_{s=1}^kW sum_{t=1}^kH weight[s][t][l][k]
                              * input[dW*(i-1)+s)][dH*(j-1)+t][l]
```

<a name='optim.sgd'></a>
### [x] sgd(opfunc, x, state)

An implementation of Stochastic Gradient Descent (SGD).

Arguments:

* `opfunc` : a function that takes a single input (`X`), the point of a evaluation, and returns `f(X)` and `df/dX`
* `x`      : the initial point
* `config` : a table with configuration parameters for the optimizer
* `config.learningRate`      : learning rate
* `config.learningRateDecay` : learning rate decay
* `config.weightDecay`       : weight decay
* `config.weightDecays`      : vector of individual weight decays
* `config.momentum`          : momentum
* `config.dampening`         : dampening for momentum
* `config.nesterov`          : enables Nesterov momentum
* `state`  : a table describing the state of the optimizer; after each call the state is modified
* `state.learningRates`      : vector of individual learning rates

Returns :

* `x`     : the new x vector
* `f(x)`  : the function, evaluated before the update

<a name='optim.dok'></a>
# Optim Package

This package provides a set of optimization algorithms, which all follow
a unified, closure-based API.

This package is fully compatible with the [nn](http://nn.readthedocs.org) package, but can also be
used to optimize arbitrary objective functions.

For now, the following algorithms are provided:

* [Stochastic Gradient Descent](#optim.sgd)
* [Averaged Stochastic Gradient Descent](#optim.asgd)
* [L-BFGS](#optim.lbfgs)
* [Congugate Gradients](#optim.cg)
* [AdaDelta](#optim.adadelta)
* [AdaGrad](#optim.adagrad)
* [Adam](#optim.adam)
* [AdaMax](#optim.adamax)
* [FISTA with backtracking line search](#optim.FistaLS)
* [Nesterov's Accelerated Gradient method](#optim.nag)
* [RMSprop](#optim.rmsprop)
* [Rprop](#optim.rprop)
* [CMAES](#optim.cmaes)

All these algorithms are designed to support batch optimization as
well as stochastic optimization. It's up to the user to construct an
objective function that represents the batch, mini-batch, or single sample
on which to evaluate the objective.

Some of these algorithms support a line search, which can be passed as
a function (L-BFGS), whereas others only support a learning rate (SGD).
