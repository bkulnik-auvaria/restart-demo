name=list(input('Input a text: '))
print(''.join(name[::-1]))


word = input("Please enter a word: ")


# Also detect Palindroms
# Example: ABBA is palindrom, because if you reverse it, its the same 


rword = ""
step = len(word)
while step > 0:
    rword = rword + word[step-1]
    step = step - 1

rword2 = ""
n = len(word)
for step in range(n):
    rword2 = rword2 + word[n-1-step]


for step in range(n):
    letter_from_the_start = word[step]
    letter_from_the_end = word[n-1-step]
    if letter_from_the_start != letter_from_the_end:
        print("Its not a palindrom!")


if word == rword:
    print("Its a palindrom!")

print(word[::-1])
print(rword)
print(rword2)
print(''.join(reversed(word)))

test = ','.join(["a","b","c"]) # inverse of split()

print(test)

