def is_unique(a) -> bool :
	b = sorted(a)
	for n in range(len(b)-1) :
		if b[n] == b[n+1] :
			return False
	return True
    
    
print(is_unique(input("Write a string: ")))