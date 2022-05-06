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

# Add dataset image (batched), model 
tb.add_image("images", grid)

# CNN Representation. Feed the data to be fed in
tb.add_graph(model, images)


```

## Hyperparameter Tuning

```python
from itertools import product
parameters = dict(
    lr = [0.01, 0.001],
    batch_size = [32,64,128],
    shuffle = [True, False]
)

param_values = [v for v in parameters.values()]
print(param_values)

for lr,batch_size, shuffle in product(*param_values):
    print("run id:", run_id + 1)
    model = CNN().to(device)
    train_loader = torch.utils.data.DataLoader(train_set,batch_size = batch_size, shuffle = shuffle)
    optimizer = opt.Adam(model.parameters(), lr= lr)
    criterion = torch.nn.CrossEntropyLoss()
    comment = f' batch_size = {batch_size} lr = {lr} shuffle = {shuffle}'
    tb = SummaryWriter(comment=comment)
    
    for epoch in range(10):
        for images, labels in train_loader:
            ...

        tb.add_scalar("Loss", total_loss, epoch)
        tb.add_scalar("Correct", total_correct, epoch)
        tb.add_scalar("Accuracy", total_correct/ len(train_set), epoch)

        # Generate histogram for all model parameters
        for name, weight in model.named_parameters():
            tb.add_histogram(name,weight, epoch)
            tb.add_histogram(f'{name}.grad',weight.grad, epoch)
    tb.add_hparams(
            {"lr": lr, "bsize": batch_size, "shuffle":shuffle},
            {
                "accuracy": total_correct/ len(train_set),
                "loss": total_loss,
            },
    )

tb.close()
```

Output:
![Training Loss Graphs](https://user-images.githubusercontent.com/38335479/167227040-a4e8bd90-4d5b-4a5f-a886-6bc190ff785c.png)
![Hyperparameter Graph](https://user-images.githubusercontent.com/38335479/167227051-73bda49f-c0b0-4750-8189-b09355d3d4d1.png)


