# Pascal's Triangle

Pascals triangle is formed like this:

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
...
```

Every element in the line is the sum of the two elements diagonally above (parents). At the edges, where no two diagonal parents above exists, a '1' is added.

Write a function that gets an integer `n` and returns the `n`-th line of the triangle.


_Hint_: To calculate the `n`-th line, you can add all pairs from the `n-1` -th line