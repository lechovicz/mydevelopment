import math
result=[]
C=50
H=30
D=raw_input('provide values of D:').split(',')
values=[i for i in D]
for D in values:
    result.append(int(round(math.sqrt((2*C*float(D))/H))))
print result
'''
calc=((2*C*D)/H)**0.5
print calc
'''