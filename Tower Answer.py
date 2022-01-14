# -*- coding: utf-8 -*-
"""
@author: artyomshutoff
"""

from random import randint

def find_num(kratno, ostatok, nyzhnie_ostatok):
	if ostatok == nyzhnie_ostatok:
		return 0
	for i in range(kratno):
		if nyzhnie_ostatok == (ostatok + i) % kratno:
			return i

colors = [randint(0, 3) for i in range(4)]
select = []

r1 = sum(colors[1:]) % 4
select.append(find_num(4, r1, 0))

r2 = (sum(colors[2:]) + colors[0]) % 4 
select.append(find_num(4, r2, 1))

r3 = (sum(colors[:2]) + colors[-1]) % 4
select.append(find_num(4, r3, 2))

r4 = sum(colors[:3]) % 4
select.append(find_num(4, r4, 3))

for i in range(4):
	if colors[i] == select[i]:
		print('Угадал', i + 1, 'мудрец')
#print(colors)
#print(select)