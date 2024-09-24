def is_unique(a) -> bool :
	b = set()
	for n in range(len(a)) :
		if a[n] not in b :
			b.add(a[n])
		else : 
			return False
	return True
    
    
print(is_unique(input("wirte a string: ")))