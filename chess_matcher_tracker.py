#from collections import counter
from itertools import combinations
from math import comb

class Player():

    total_players = 0
    list_of_players = []

    def __init__(self, name) -> None:
        self.name = name
        self.games = []  #[(Freddy, 0), (Jochem, 1)]
        Player.list_of_players.append(self.name) #append this player to the list of all players 
        Player.total_players += 1 
        super().__init__()
    
    def get_name(self) -> str:
        #return '{}'.format(self.name)
        return self.name

    def get_games(self) -> str:
        #return '{}'.format(self.name)
        return self.games
    
    def played_games(self):
        return len(self.games)
    
    def update_games(self, player, score):
        self.games.append((player, score))
    
    def get_current_stats(self):
        return 
    
    @classmethod
    def get_all_games(cls):
        all_games = combinations(cls.list_of_players, 2)
        return list(all_games)




class Game():
    
    total_games = []

    def gameplayed(self, winner_score):
        if winner_score[2] >= 2:
            return '0:first_player_wins, 1:second_player_wins, 2:draw'
        #winner_score (Jochem, Freddy, 1) 0:first_player_wins, 1:second_player_wins, 2:draw
        
        self.total_games.append(winner_score)
        #(Jochem, Freddy, 0) - jochem wins against freddy
        player1 = winner_score[0]
        player2 = winner_score[1]
        if winner_score[2] == 2:
            player1.update_games(player2, 0.5)
            player2.update_games(player1, 0.5)
        elif winner_score[2] == 0:
            player1.update_games(player2, 1)
            player2.update_games(player1, 0)
        elif winner_score[2] == 1:
            player1.update_games(player2, 0)
            player2.update_games(player1, 1)

    @classmethod
    def get_total_games(cls):
        games = []
        for game in cls.total_games:
            games.append((game[0].name, game[1].name, game[2]))
        return games
    


    


#player_games = [(Freddy, 0), (Jochem, 1)]

#First: Create all players 
Freddy = Player('Freddy')
Jochem = Player('Jochem')
Stan = Player('Stan')



#Second: Get all Games
all_games_to_play = Player.get_all_games()
print(all_games_to_play)

current_games = []
current_games.append(all_games_to_play[0])
number_of_games = comb(Player.total_players,2)
current_games.append(all_games_to_play[number_of_games-1])
print(number_of_games)


print(current_games)
#10games, last 3
#6 games, last 1 (player 1 takes 3, player 2 takes 2)







#Freddy.update_games(Jochem, 1)
#game1.update_games(Jochem, 1) -> 
newGame = Game().gameplayed((Freddy, Jochem, 0))
#newGame2 = Game().gameplayed((Stan, Alexis, 1))




#print(f"Games to play: {Player.get_all_games()}")
#print(f"All Player: {Player.total_players}")
#print(Freddy.__dict__)
#print(Freddy.get_name())
#print(Freddy.get_games())
#print(Freddy.played_games())