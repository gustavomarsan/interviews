# Class  Appoint has a list of 24 hour set in 0s. and a number of meeting already scheduled. 
# If an appointment is schedule (by method schedule(hour, long) ) then move 1 to the list space and  add 1 to  meeting acum
# in case there isn't an appointment in this hour yet. (the list space was 0).
# If the appointment to schedule is more than 1 hour long, then use the next hours too.
# method is_full() returns if there is free space for schedule more appointments. 
# Appointments should begin in exact hour.
# in this case we use a list in O(1) complexity because we don´t read the whole list, we acces it directly the index



class Appoint:
    def __init__(self) -> None :
        self.hours = [0] * 24
        self.meetings = 0
        
    def schedule(self, init: float, long: float) -> None :
        while long > 0 :
            if self.hours[init] == 0 :
                if long > 1 :
                    self.hours[init] = 1
                else :
                    self.hours[init] = long
                self.meetings += 1
            long -= 1
            init += 1

    def is_full(self) -> bool :     # check is there a free space for an appoinment
        return self.meetings == 24
    
a = Appoint()

print(a.hours)
a.schedule(0,1)
a.schedule(4, 1.5)
a.schedule(12, 1.5)
a.schedule(23, 1)
a.schedule(10, 2)
a.schedule(9, 1)
a.schedule(22, 1)

#print("Is full:", Appoint.is_full(a))


print(a.hours)
print("Is full:", Appoint.is_full(a))

for n in range(24) :
    if a.hours[n] == 0 :
        a.schedule(n, 1) 

print(a.hours)
print("Is full:", Appoint.is_full(a))

