import random
#Team 1
players = ["Martain", "Craig", "Sue", "Claire", "Dave", "Alice", "Luciana",
            "Harry", "Jack", "Rose", "Lexi", "Maria", "Thomas",
            "James", "William", "Ada", "Grace", "Jean", "Marissa", "Alan"]
print("Welcome to Team Allocator")
while True:
 random.shuffle(players)
 team1 = players[:len(players)//3]
 print("Team 1 captain: " + random.choice(team1))
 print("Team 1: ")
 for player in team1:
    print(player)

 #Team 2
 team2 = players[len(players)//3: (len(players)//3*2)]
 print("\nTeam 2 captain: "+ random.choice(team2))
 for player in team2:
    print(player)
 team3 = players[(len(players)//3)*2:]
 print("\nTeam 3 captain: " + random.choice(team3))
 print("Team 3:")
 for player in team3:
   print(player)

 response = input("Pick teams again? Type y or n: ")
 if response == "n" : 
   break
