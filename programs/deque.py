from collections import deque

teams = ["Manchester United", "Chelsea", "Tottenham", "Arsenal"]
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

print(premier_league)
