import random
from itertools import combinations
import math



#Create a list of all game combinations

def calculate_games(players):
	future_games = list(combinations(players,2))
	random.shuffle(future_games)
	#print(f"There will be {len(future_games)} games which are : {future_games}")
	#print(f"All Players: {players}")
	#Number of rounds:
	number_of_player_per_round = round(len(players))
	if number_of_player_per_round % 2 == 1:
		number_of_player_per_round -= 1
	number_rounds = math.ceil(len(future_games)/(number_of_player_per_round/2))
	return number_rounds, future_games


def calculate_current_round(future_games):
	current_games = []
	current_player = set()
	if len(future_games) > 0:
		nex_game = future_games.pop(0)
		current_games.append(nex_game)
		current_player.update([nex_game[0], nex_game[1]])
		# Iterate over remaining tuples and select those that meet the condition
		#print([t for t in future_games if not (0 in t or 1 in t)])
		for idx, game in enumerate(future_games):
			#future_games: [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
			#current_games: (0, 1)
			#print(f"current players: {current_player}")

			if game[0] in current_player or game[1] in current_player:
				#print(f"Skip this game ({game}) because Players already play")
				continue 

			else:

				#print(f"Enter else because current game: {game[0]} and {game[1]}")
				#print(f"and current players: {current_player}")
				next_game = future_games.pop(idx)
				#print(f"Remove {game} from future games: {future_games}")
				current_player.update([next_game[0], next_game[1]])
				#print(f"Update Player: {current_player}")
				#print(f"next_game: {next_game}")
				#print(f"current games: {current_games}")
				#print(f"future_games: {future_games}")
				current_games.append(next_game)
				#print(f"update current games: {current_games}")

	return current_games, future_games, current_player

def game_round(future_games,number_rounds, past_games):
	print(f"There will be {number_rounds} rounds!")
	for index, runde in enumerate(range(int(number_rounds))):
		print(f"\ncurrent Round {index}: ")
		current_games, future_games, current_player = calculate_current_round(future_games)
		print(f"current Games: {current_games}")
		print(f"future Games: {future_games}")
		past_games.extend(current_games)
		print(f"past Games: {past_games}")
	return future_games, current_games, past_games

