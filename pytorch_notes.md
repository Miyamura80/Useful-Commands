# Pytorch Notes



## CPU/GPU

`tensor.cuda()` is used to move a tensor to GPU memory.
`tensor.cpu()` moves it back to memory accessible to the CPU.

## Squeeze

`torch.squeeze(n: int)`, `torch.tensor.squeeze(n: int)` wraps all element/arguments in a larger box 

```
>>> x = torch.tensor([1, 2, 3, 4])
>>> torch.unsqueeze(x, 0)
tensor([[ 1,  2,  3,  4]])
>>> torch.unsqueeze(x, 1)
tensor([[ 1],
        [ 2],
        [ 3],
        [ 4]])
```


## Numpy


`tensor.numpy()` convert tensor to numpy array

Note: They share the same memory location. For example:
```python
a = torch.ones(5)
b = a.numpy()
a.add_(1)
print(a)
print(b)
```

Out:
```
tensor([2., 2., 2., 2., 2.])
[2. 2. 2. 2. 2.]
```
