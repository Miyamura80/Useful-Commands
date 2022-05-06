# TensorBoard
```python
from torch.utils.tensorboard import SummaryWriter
tb = SummaryWriter('runs/folderName')

...
```

Then, run tensorboard:
```
tensorboard --logdir runs
```


## CNN Example
```python
model = CNN()

# Dataset specific 
images, labels = next(iter(train_loader))
grid = torchvision.utils.make_grid(images)

# Add image, model 
tb.add_image("images", grid)
tb.add_graph(model, images)
tb.close()
```


