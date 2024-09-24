def move_zeroes(a) :
	rows = set()
	cols = set()
	for x in range(len(a)) :
		for y in range(len(a[x])) :
			if a[x][y] == 0 :
				cols.add(y)
				rows.add(x)
	for x in range(len(a)) :
		for y in range(len(a[x])) :
			if y in cols or x in rows :
				a[x][y] = 0
	for x in range(len(a)) :
		print(a[x])
				
        
        
a = [
  	  [25, 18, 30, 40, 52],
  	  [32, 19, 44, 12,  9],
      [ 0,  3, 10, 48,  7],
      [ 2, 20,  8, 16,  0],
      [23, 14, 22, 11, 34]
      ]

print(move_zeroes(a))