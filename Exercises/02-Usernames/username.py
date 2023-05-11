import random
import string
with open(r'C:\Users\dci-student\Documents\GitHub\restart-demo\Exercises\02-Usernames\english-adjectives.txt') as f:
    adjective=f.read().split()
with open(r'C:\Users\dci-student\Documents\GitHub\restart-demo\Exercises\02-Usernames\english-nouns.txt') as f:
    noun=f.read().split()

h=0
while h!='1':
    x=random.choice(adjective)
    y=random.choice(noun)
    print(x+' '+y)
    h=input('If you like this name insert 1: ')
    
low_alph=list(string.ascii_lowercase)
up_alph=list(string.ascii_uppercase)
nums=[str(x) for x in range(10)]
special=list('''`~!@#$%^&*()_-+={[]}|\:;"'<,>.?/''')

n1=random.randint(1,29)
p1=random.choices(low_alph,k=n1)
n2=random.randint(1,30-n1)
p2=random.choices(up_alph,k=n2)
n3=random.randint(1,31-n2-n1)
p3=random.choices(nums,k=n3)
n4=32-n1-n2-n3
p4=random.choices(special,k=n4)
p=p1+p2+p3+p4
random.shuffle(p)
print(''.join(p))

