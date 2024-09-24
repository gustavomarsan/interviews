"""""
With a plater class (name, score), given a list o players, order the list in descendent order from the score
and in there are two players with de same score, order by name (ascendent).

To check wich player has higher score, implemente a methos in a class checker. if a <= b return -1
                                                                                if a > b return 1

list =[[John, 100], [Daniel, 150], [Fred, 150], [Alicia, 100],[Bob, 50]]
return
list =[[Daniel, 150], [Fred, 150], [Alicia, 100], [John, 100], [Bob, 50]]

"""
class Player:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score


class Checker:
    def compare(a: Player, b: Player)-> int :           # -1 should swicth a y b.   1 shouldn't wicth a y b
        if a.score < b.score :
            return -1
        if a.score == b.score and a.name > b.name :
            return -1
        if a.score == b.score and a.name < b.name :
            return 1
        if a.score > b.score :
            return 1
        
list = []
for n in range(5):
    a = Player(input("Nombre: "), int(input("Score: ")))
    list.append(a)

for n in range(len(list)):
    print(list[n].name, list[n].score, end=" ")
print()

sorted =  False
while not sorted :                  # initialize loop for a bubble sort, repeat until list is sorted
    sorted = True
    for n in range(len(list)-1) :   # walk the list from the beginning to the end
        if Checker.compare(list[n], list[n+1]) == -1 :          # -1 swicth a y b, 1 no wicth a y b
            sorted =  False
            temp = list[n]
            list[n] = list[n+1]
            list[n+1] = temp
        

for n in range(len(list)):
    print(list[n].name, list[n].score, end=" ")
print()

            
