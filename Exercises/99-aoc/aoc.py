with open(r'C:\Users\dci-student\Documents\GitHub\restart-demo\Exercises\99-aoc\puzzle_input.txt') as f:
    lines=f.readlines()

with open(r'C:\Users\dci-student\Documents\GitHub\restart-demo\Exercises\99-aoc\example.txt') as f:
    lines2=f.readlines()

main={}
marker=[]
dirsize={}

for x in lines:
    l=x.split()
    if l[0]!='$':
        dir=main
        for x in marker:
            dir=dir[x]
        if l[0]=='dir':
            dir[l[1]]={}
        else:
            dir[l[1]]=int(l[0])
    elif l[1]=='cd':
        if l[2]=='..':
            dir=main
            for x in marker:
                dir=dir[x]
            a=marker[-1]
            dirsize[a]=sum(dir.values())
            marker.pop()
            dir=main
            for x in marker:
                dir=dir[x]
            dir[a]=dirsize[a]
        elif l[2]!='/':
            marker.append(l[2])

while len(marker)!=0:
    dir=main
    for x in marker:
        dir=dir[x]
    a=marker[-1]
    dirsize[a]=sum(dir.values())
    marker.pop()
    dir=main
    for x in marker:
        dir=dir[x]
    dir[a]=dirsize[a]

dirsize['/']=sum(dir.values())
print(dirsize)
    

