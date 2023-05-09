# Example Username Generator

Write a program that generates random usernames.

A username should be generated randomly by combining an adjective and a noun.
A predefined list of adjectives and nouns should be used which will be loaded via a file.

For the username, e.g. download the following files or use the ones in the repository
- https://github.com/hugsy/stuff/blob/main/random-word/english-nouns.txt
- https://github.com/hugsy/stuff/blob/main/random-word/english-adjectives.txt



**Part 1**: Write a python script that loads the data from the files and generates a random username

**Part 2**: Make an interactive menu, that asks the user if he/she wants another username or quit the program.

**Part 3 (Bonus)**: Additional to the username, the program should also generate a password 



_Hint_:

To generate random numbers, use the `random` module.

```python
import random

random.randint(0,10) # will generate a random int from 0 to 10 (including both end points)
```