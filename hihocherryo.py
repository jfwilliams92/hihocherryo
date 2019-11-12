import random

class Game():
    def __init__(self, num_players):
        
        try:
            assert 0 < num_players <= 4, 'Number of players should be between 1 and 4'
        except AssertionError as ae:
            raise 
        
        self.num_players = num_players
        player_options = ["Blueberries", "Apples", "Grapes", "Oranges"]
        random.shuffle(player_options)
        self.players = [Player(color=c) for c in player_options[:num_players]]

        self.gamewheel = GameWheel()

    def play_game(self):
        continue_play = True
        current_player_ix = 0
        while continue_play:
            current_player = self.players[current_player_ix]
            print(f"{current_player.color}' turn!")
            print(f"{current_player.color}' basket has {current_player.basket}")
            print(f"{current_player.color}' tree has {current_player.tree}")
            
            continue_play = current_player.play_turn(self.gamewheel)
            current_player_ix = current_player_ix + 1 if current_player_ix < self.num_players else 0

        print("Game over!")


class Player():
    def __init__(self, color):
        self.basket = 0
        self.tree = 10
        self.color = color

    def play_turn(self, gamewheel):
        choice, consequence = gamewheel.spin_wheel()
        print(f"The wheel landed on {choice} for {self.color}")

        self.basket += consequence
        if self.basket < 0:
            self.basket = 0
        elif self.basket >= 10:
            print(f"{self.color} won the game!")
            
            return False

        self.tree -= consequence
        if self.tree > 10:
            self.tree = 10

        return True

class GameWheel():
    """
    A simple spin wheel with 6 choices.
    """
    def __init__(self):
        self.choices = {
            "1": 1,
            "2": 2,
            "basket_tip": -10,
            "4": 4,
            "dog": -2,
            "3": 3,
            "bird": -2            
        }
    
    def spin_wheel(self):
        choice = random.choice(list(self.choices.keys()))
        choice_consequence = self.choices[choice]

        return choice, choice_consequence



