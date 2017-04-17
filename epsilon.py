#1----s----1+2 a la -29
#1+s=, s!=0
s=1
for i in range(100):
	s=0.5*s
	t=1+s
	#print(s)
	if t<=1:
		s=2*s
		print(s)
		break
