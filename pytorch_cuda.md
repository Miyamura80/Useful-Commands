# CUDA 

TLDR: Need both tensor and network to be on device

## CUDA on tensors

```python
t1 = torch.tensor([[1,2],[3,4]])
t2 = torch.tensor([[5,6],[7,8]])

t1.device, t2.device
```

To move tensor onto CUDA, do:
```python
t1 = t1.to('cuda')
t1.device
```

The index specifies which GPU it is using

## CUDA on networks

```python
test_net.to('cuda')
for name, param in test_net.named_parameters():
    print(name, '\t\t\t', param.device)
```
