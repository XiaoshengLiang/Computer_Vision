group_name=raw_input()
comet_name=raw_input()

groups=list(group_name)
comets=list(comet_name)

g=c=1

for group in groups:
	g=(ord(group))*g
for comet in comets:
	c=(ord(comet))*c

if (g%47)==(c%47):
	print 'GO'
else:
	print 'STAY'
