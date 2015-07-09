f=open('barn1.in','r')
para=f.readline().split(' ')
M=int(para[0])
S=int(para[1])
C=int(para[2])

line=[]
distance_line=[]
lines=f.read().split('\n')
for i in range(C):
	line.append(int(lines[i]))
for i in range(1,C):
	distance=line[i]-line[i-1]
	distance_line.append(distance)
distance_line.sort()

length=int(line[C-1])-int(line[0])+1

distance_line=distance_line[::-1]
for i in range(M-1):
	length-=(distance_line[i]-1)

f1=open('barn1.out','w')
f1.write(str(length)) 
f1.close()	
