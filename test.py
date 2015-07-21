__author__ = 'mohanchintamanapinna'
t=[]
with open('README.md','r') as f:
    lines=f.readlines()
    for i in lines:
        t.append(i)
c=0

foos = [1.0,2.0,3.0,4.0,5.0,6.0]
bars = [1,2,3,4,5]
for x1, x2 in zip(foos, bars):
    print x1,x2





