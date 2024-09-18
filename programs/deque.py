from collections import deque

teams = ["Manchester United", "Chelsea", "Tottenham", "Arsenal"]
print(teams)
teams2 = ["Sheffield", "Newcastle", "Lutton"]
premier_league = deque(teams)

print(premier_league)
premier_league.appendleft("Wolverhamptom")
premier_league.append("West Ham")

print(premier_league)

premier_league.extendleft(teams2)

print(premier_league)

print(premier_league.count("Chelsea"))

premier_league.insert(2, "Blackburn")


premier_league.appendleft("West Ham")
print(premier_league)
print("Place of West ham is: ", premier_league.index("West Ham"))
print(premier_league.count("West Ham"))

b = deque()
print(b)
b.append("Brighton")
b.appendleft("Ipswich")

premier_league.extend(b)
print(premier_league)
print(len(premier_league))