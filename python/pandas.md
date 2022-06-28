# Pandas

```python
import pandas as pd
df = ...
print(df.to_string())
```
## From CSV

```python
df = pd.read_csv('data.csv')

```


## From dictionary

```python
data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
df = pd.DataFrame.from_dict(data)
df.head(4)
```

```
   col_1 col_2
0      3     a
1      2     b
2      1     c
3      0     d
```

Orient using `pd.DataFrame.from_dict(data, orient="index")` to get rows, not columns
