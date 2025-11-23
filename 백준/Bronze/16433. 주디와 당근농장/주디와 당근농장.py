n, r, c = map(int, input().split())

for i in range(n):
	for j in range(n // 2):
		if (r % 2 == 0 and c % 2 == 0) or (r % 2 != 0 and c % 2 != 0):
			if i % 2 != 0:
				print('.v', end='')
			else:
				print('v.', end='')
		else:
			if i % 2 == 0:
				print('.v', end='')
			else:
				print('v.', end='')
    
	if n % 2 != 0:
		if (r % 2 == 0 and c % 2 == 0) or (r % 2 != 0 and c % 2 != 0):
			if i % 2 != 0:
				print('.', end='')
			else:
				print('v', end='')
		else:
			if i % 2 == 0:
				print('.', end='')
			else:
				print('v', end='')
	print()