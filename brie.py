# code to divide your triangle brie into n equal parts
import argparse
import numpy as np

def height_as_root(a1, tgalpha, s):
	num = -a1 + (a1*a1 + 4*tgalpha*s)**0.5
	den = 2*tgalpha
	return num/den

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--base', type=float)
parser.add_argument('-b', '--height', type=float)
parser.add_argument('-n', '--number', type=int)
args = parser.parse_args()

a = args.base
h = args.height
n = args.number

S = 0.5*a*h
s = S/n

#print(S, s)

heights = [h/n**0.5]
bases = [a/n**0.5]
tgalpha = a/h

for i in range(n-1):
	a1 = bases[-1]
	h2 = height_as_root(a1, tgalpha, s)
	a2 = a1 + 2*h2*tgalpha
	heights.append(h2)
	bases.append(a2)
#areas = 0.5*(np.array(bases[:-1])+np.array(bases[1:]))*np.array(heights[1:])
result = [round(hei,1) for hei in heights]
#print('heights\n', heights)
#print('bases\n', bases)
#print('areas\n', areas)
print("To divide your triangle piece of brie with the height of {} and base of {} into {} equal parts, use the following heights:". format(h,a,n))
print(result)

