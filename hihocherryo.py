import random

class HiHoCherryO():

    def __init__(self, num_players, verbose=True):
        
        """
        A HiHoCherryO game that continues until one player achieves 10 fruit in basket
    
        Args:
            num_players (int): The number of players in the game, between 1 and 4
            verbose (bool): indicates whether game should print to screen with interim results
        """

        # num players should be a valid choice
        try:
            assert 0 < num_players <= 4, 'Number of players should be between 1 and 4'
        except AssertionError as ae:
            raise 
        
        self.num_players = num_players
        
        # fruit options, shuffled
        player_options = ["Blueberries", "Apples", "Grapes", "Oranges"]
        random.shuffle(player_options)
        # create game's players
        self.players = [Player(fruit=f) for f in player_options[:num_players]]

        self.gamewheel = GameWheel()

        self.num_turns = 0
        self.num_rounds = 0
        self.verbose = verbose

    def play_game(self, interactive=True):
        """
        Play the game until one player wins (has 10 fruit in basket).
        
        Args:
            interactive (bool): indicates whether the game should proceed with or without 
            user input (default True)

        Returns:
            num_rounds (int): The number of times around the Player circle before game ended.
            num_turns (int): The total number of turns taken in the game.
            winner_fruit (string): the fruit choice of the winning player
            winner_ix (int): the index of the winning player (e.g. 0 == Player 1)
        """

        continue_play = True
        current_player_ix = 0
        
        # loop until continue_play == False, ie until current_player.play_turn returns False
        while continue_play:
            if current_player_ix == 0:
                self.num_rounds += 1
            self.num_turns += 1

            current_player = self.players[current_player_ix]
            
            if self.verbose:
                print(f"\n{current_player.fruit}' turn!")
                print(f"{current_player.fruit}' basket has {current_player.basket}")
                print(f"{current_player.fruit}' tree has {current_player.tree}")
            
            # current player takes a turn
            continue_play = current_player.play_turn(self.gamewheel, self.verbose)
            
            if self.verbose:
                print(f"{current_player.fruit}' basket has {current_player.basket}")
                print(f"{current_player.fruit}' tree has {current_player.tree}")
            
            if continue_play:
                # iterate to next player
                current_player_ix = current_player_ix + 1 if current_player_ix < (self.num_players - 1) else 0

                # wait for input if in interactive mode
                if interactive:
                    input(f"Press any button to play {self.players[current_player_ix].fruit}' turn!")

        if self.verbose:
            print("Game over! Hi ho Cherry-O!!!")
        
        return self.num_rounds, self.num_turns, current_player.fruit, current_player_ix

class Player():
    
    def __init__(self, fruit):
        """
        A player of the Hi-Ho-CherryO game.

        Args:
            fruit (string): the fruit choice of the player, involuntary
        """
        
        self.basket = 0
        self.tree = 10
        self.fruit = fruit
        self.num_turns = 0

    def play_turn(self, gamewheel, verbose):
        """
        Player spins the gamewheel and draws a consequence.
        If the consequence is positive, fruit is moved from tree
        to basket. If the consequence is negative, fruit is moved from 
        basket to tree. Basket and Tree can never hold more than 10 
        or less than 0 fruit.

        Args:
            gamewheel: HiHoCherryO Gamewheel
            verbose (bool): indicates whether to print results or not
        
        Returns:
            continue_play (bool): indicates whether game should continue or not
        """

        self.num_turns += 1
        
        # Player spins wheel
        choice, consequence = gamewheel.spin_wheel()
        if verbose:
            print(f"The wheel landed on {choice} for {self.fruit}")

        # Player substracts consequence from tree.
        self.tree -= consequence
        if self.tree > 10:
            self.tree = 10
        
        # Player adds consequence to basket. If basket >= 10, game is over and continue_play is False
        self.basket += consequence
        if self.basket < 0:
            self.basket = 0
        elif self.basket >= 10:
            if verbose:
                print(f"{self.fruit} won the game!")
            
            return False

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
        """
        Spin the game wheel and draw a consequence.

        Args:
            None

        Returns:
            choice (string): string representation of the result
            consequence (int): numerical representation of result
        """

        choice, consequence = random.choice(list(self.choices.items()))
        return choice, consequence





