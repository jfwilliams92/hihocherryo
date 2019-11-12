# test to see how long it takes to play different permutations of the game
# some test plots, will move to a Jupyter Notebook
import hihocherryo
import matplotlib.pyplot as plt
from collections import Counter

all_game_stats = {}

for num_players in range(1, 5):
    stats = {
        "num_rounds": [],
        "num_turns": [],
        "winner": [],
        "winner_ix": []
    }

    for game in range(100000):
        g = hihocherryo.HiHoCherryO(num_players=num_players, verbose=False)
        num_rounds, num_turns, winner, winner_ix = g.play_game()
        stats["num_rounds"].append(num_rounds)
        stats["num_turns"].append(num_turns)
        stats["winner"].append(winner)
        stats["winner_ix"].append(winner_ix)

    all_game_stats[num_players] = stats


fig, ax = plt.subplots(2, 2, figsize=(15,15))
ax = ax.flatten()
for num_players in range(1, 5):
    num_rounds_list = all_game_stats[num_players]["num_rounds"]
    ax[0].hist(num_rounds_list, bins=50, alpha=0.25, density=True, label=num_players, cumulative=True)
    ax[0].legend()
    ax[0].set_title('Cumulative hist of number of rounds to game completion by num players')

    ax[1].hist(num_rounds_list, bins=50, alpha=0.25, density=True, label=num_players)
    ax[1].legend()
    ax[1].set_title('Number of rounds to game completion by num players')


    num_turns_list = all_game_stats[num_players]["num_turns"]
    ax[2].hist(num_turns_list, bins=50, alpha=0.25, density=True, label=num_players)
    ax[2].legend()
    ax[2].set_title('Number of total turns to game completion by num players')

    ax[3].hist(num_turns_list, bins=50, alpha=0.25, density=True, label=num_players, cumulative=True)
    ax[3].legend()
    ax[3].set_title('Cumulative hist of total turns to game completion by num players')

fig, ax = plt.subplots(2, 2, figsize=(15,15))
ax = ax.flatten()
for num_players in range(1, 5):
    winner_ix_count = Counter(all_game_stats[num_players]["winner_ix"])
    keys = list(winner_ix_count.keys())
    counts = list(winner_ix_count.values())
    ax[num_players - 1].bar(keys, counts, tick_label=keys)
