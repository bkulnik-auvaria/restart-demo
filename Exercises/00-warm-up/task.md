# Warm Up Tasks

Do you know what the following statements do?
If not, test them!


---


```python
x = ["a","b","c"]
len(x)
```


---

```python
"hello".upper()
```


---

```python
print("What do these '\\n' mean? \n\n Can you find out?")
```

---

```python
"2+3={}".format(2+3)
```

---

```python
2 ** 3 == 2 * 2 * 2
```

---

```python
"x=1;y=2;z=3".split(";")
```

---

```python
with open("prices.csv") as f:
    content = f.read()

f = open("prices.csv")
f.read()
f.close()

lines = content.splitlines()
for line in lines:
    line.split(",")

```

---

```python
x = ['apple', 'bananas', 'oranges', 'peas', 'grapes']
x[1:2]
x[0:5:2]
x[::-1]
```