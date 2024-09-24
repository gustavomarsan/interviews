# este programa Crea un set llamado "club", que contenga los números 3, 22, 54, 93 
# (números de los miembros que ya pagaron)


#club = set()    esto crearia un set vacio, 
club = {3, 22, 54, 93, 0, "orange" }

print("1 en club?" )
print(1 in club)
print("22 en club?" )
print(22 in club)
club.add(1)
club.add("lemon")
print(club)
club.remove(93)
print(club)