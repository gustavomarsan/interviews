"""
Given an array of integers, return how many sub arrays of lenght 2 or greater that have non-repeated numbers

a = [1, 2, 3, 3, 2, 2, 1]				p1          p2			c
										2 			3		   3
                                        
                                        set = {3}
-> 5

[1, 2]
[1, 2, 3]
[2, 3]
[3, 2]
[2, 1]

space: O(n)

sliding window
O(n)

[

"""
def how_many_subs(a: list)-> int :
  my_set = set()
  c = 0
  p1 = 0
  p2 = 0
  while p1 < len(a) -1 and p2 < len(a):
    if a[p2] not in my_set :
        my_set.add(a[p2])
        c += (p2-p1)
        p2 += 1
    else :
      my_set.clear()
      p1 = p2
  return c
      

a = [1, 2, 3, 3, 2, 2, 1, 3]

print(how_many_subs(a))