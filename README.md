A simple implementation of a simple game.

Hi Ho Cherry-O! is a children's board game with 1-4 players.
Each player starts the game with 10 pieces of fruit in their tree, with the objective of the game being to collect all the fruit from their tree into their basket.
During each player's turn, he/she spins the game wheel and takes the corresponding action. 
The actions are as follows:
  - 1 - Add 1 fruit from tree to basket
  - 2 - Add 2 fruit from tree to basket
  - 3 - Add 3 fruit from tree to basket
  - 4 - Add 4 fruit from tree to basket
  - Dog - Remove 2 fruit from basket and put on tree
  - Bird - Remove 2 fruit from basket and put on tree
  - Basket Tip - All fruit removed from basket and replaced on tree

The first player to get all 10 pieces of fruit from their tree to their basket wins!

As you can surmise, this appears to be a game of pure chance. It is a special favorite of my 4 year old son and my 2 year old daughter, and it seemed like good practice for exploring different aspects/applications of Python programming, including:
  - Python standard library (instead of relying exclusively on NumPy ;b )
  - Python classes and objects
  - Monte Carlo Simulations, since this is a game of chance
  - (future version) Simple GUI and I/O programming

In this repo I'll look at a couple of things data-wise, including how many rounds/turns I can expect to play in a game of HHC with 1-4 players, and if there's any strategic advantage to the order in which the game starts (maybe that's the reason my 2 year old always wins...)


