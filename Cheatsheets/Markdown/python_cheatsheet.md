
# Python CheatSheet

## Main

```python
if __name__ == '__main__':
    main()
```

## Call Python File From Terminal

```python
import sys
def call_func():
sys("python script.py")
```

## Inline

### Comprehension

```python
<list> = [i for i in range(10)] #[0, 1, 2, ..., 9]
<set> = {i for i in range(10) if i > 5} # {6, 7, 8, 9,}
<dict> = {i: i*2 for i in range(10)} # {0:0, 1:2, 2:4, ..., 9:18}
```

### If-Else
```python
<expression_if_true> if <condition> else <expression_if_false>
```

```python
>>> [a if a else "zero" for a in (0, 1, 0, 3)]
["zero", 1, "zero", 3]
```

## Dictionary

```python
<view> = <dict>.keys()
<view> = <dict>.values()
<view> = <dict>.items()
```

```python
value  = <dict>.get(key, default=None)         # Returns default if key does not exist.
value  = <dict>.setdefault(key, default=None)  # Same, but also adds default to dict.
<dict> = collections.defaultdict(<type>)       # Creates a dictionary with default value of type.
<dict> = collections.defaultdict(lambda: 1)    # Creates a dictionary with default value 1.
```

```python
<dict>.update(<dict>)                          # Or: dict_a = {**dict_a, **dict_b}.
<dict> = dict(<list>)                          # Initiates a dict from list of key-value pairs.
<dict> = dict(zip(keys, values))               # Initiates a dict from two lists.
<dict> = dict.fromkeys(keys [, value])         # Initiates a dict from list of keys.
```

```python
value = <dict>.pop(key)                         # Removes item from dictionary.
{k: v for k, v in <dict>.items() if k in keys}  # Filters dictionary by keys.
```
