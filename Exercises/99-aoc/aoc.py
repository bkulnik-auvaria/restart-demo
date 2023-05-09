with open(r'C:\Users\dci-student\Documents\GitHub\restart-demo\Exercises\99-aoc\example.txt') as f:
    lines=f.readlines()

main={}
marker=[]

for x in lines:
    l=x.split()
    if l[0]!='$':
        if l[0]=='dir':
            main[l[1]]={}
        else:
            main[l[1]]=int(l[0])
    elif l[1]=='cd':
        if l[2]=='..':
            marker.pop()
        elif l[2]!='/':
            marker.append(l[2])
        print(marker)
print(main)
    

