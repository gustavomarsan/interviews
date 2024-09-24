""" 
“legacy system”

ask questions out loud after reading ?

storage (noun) -> store (verb)

What brought you to lyft?

	Why did you decide to work at lyft (instead of other companies)?
	What do you like of working at lyft?

What do you do?

	What does the day to day look like for you?


My solution

class Base:
    def __init__(self, size=10) -> None:
      	base = []
        felt = 0
        for i in range size : 
        	base[i] = False     # False is not attacked

    def attack(self, start) -> None:
      	if base[start] = False :
        	base[start] = True		# True is attacked
          felt += 1

    def is_game_over(self) -> bool:
        if felt == size :
          return True
        return False
	



Dario´s optimize

class Base:
    def __init__(self, size=10) -> None:
        self.base = [False for _ in range(size)]
        self.attacked = 0

    def attack(self, start) -> None:
        if not self.base[start] :
           self.base[start] = True		# True is attacked
            self.attacked += 1

    def is_game_over(self) -> bool:
        return self.attacked == len(self.base)





 """


class Base:
    def __init__(self, size=10) -> None:
        self.size = size
        self.base = [False for _  in range(size)]
        self.felt = 0
        #for i in range(size) : 
        #    self.base.append(False)      # False is not attacked

    def attack(self, start) -> None:
      	if not self.base[start] :
            self.base[start] = True		# True is attacked
            self.felt += 1

    def is_game_over(self) -> bool:
        return self.felt == self.size
    

    
a = Base()
a.attack(0)
print(a.base)
a.attack(1)
a.attack(2)
a.attack(3)
a.attack(4)
a.attack(5)
a.attack(6)
a.attack(6)
a.attack(8)
a.attack(9)
print(a.base)
print(a.is_game_over())