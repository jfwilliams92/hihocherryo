import random

class HiHoCherryO():
    def __init__(self, num_players):
        
        try:
            assert 0 < num_players <= 4, 'Number of players should be between 1 and 4'
        except AssertionError as ae:
            raise 
        
        self.num_players = num_players
        player_options = ["Blueberries", "Apples", "Grapes", "Oranges"]
        random.shuffle(player_options)
        self.players = [Player(fruit=f) for f in player_options[:num_players]]

        self.gamewheel = GameWheel()

        self.num_turns = 0
        self.num_rounds = 0

    def play_game(self):
        continue_play = True
        current_player_ix = 0
        while continue_play:
            if current_player_ix == 0:
                self.num_rounds += 1
            self.num_turns += 1

            current_player = self.players[current_player_ix]
            print(f"\n{current_player.fruit}' turn!")
            print(f"{current_player.fruit}' basket has {current_player.basket}")
            print(f"{current_player.fruit}' tree has {current_player.tree}")
            
            continue_play = current_player.play_turn(self.gamewheel)
            
            if continue_play:
                print(f"{current_player.fruit}' basket has {current_player.basket}")
                print(f"{current_player.fruit}' tree has {current_player.tree}")
            
            current_player_ix = current_player_ix + 1 if current_player_ix < (self.num_players - 1) else 0

        print("Game over! Hi ho Cherry-O!!!")
        
        return self.num_rounds, self.num_turns, current_player.fruit


class Player():
    def __init__(self, fruit):
        self.basket = 0
        self.tree = 10
        self.fruit = fruit

    def play_turn(self, gamewheel):
        choice, consequence = gamewheel.spin_wheel()
        print(f"The wheel landed on {choice} for {self.fruit}")

        self.basket += consequence
        if self.basket < 0:
            self.basket = 0
        elif self.basket >= 10:
            print(f"{self.fruit} won the game!")
            
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





