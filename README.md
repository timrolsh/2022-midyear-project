# 2022-midyear-project
Midyear project for AP Comp Sci, 2022. Online version of Alan R. Moon's board game, Ticket To Ride. Tools: Python3, Pygame 2.10.2.  

# How to Play
Playing our game is very simple. Please select a display width and height in the settings.json file, and specify colors for the players. As of right now, only two human players are supported in our game. In the future, we will add computer players and options to play with more than two people. 

# Ticket to Ride Rules (Explained)

[![ticket-to-ride-rules-image.png](https://i.postimg.cc/nhs3Tdct/ticket-to-ride-rules-image.png)](https://postimg.cc/XrbKYkC2)

# Setup
- Score starts at 0 for each player
- Each player has 45 train cars of the same color
- 4 cards are given to each player. Each card is one color, and the color determines where you can place a train car. 
- The remaining cards stay near the board, and 5 cards from the top of this deck are placed face up.
- Longest path bonus card is placed at the top of the deck. 
- Each player gets three destination cards, and must keep a minimum of two cards. 
Turns
- Three options
  - Draw two train cards
     - If taken from the five face-up cards at the top, one wild card (rainbow) counts for two train cards
     - If there are no more train cards, players can only claim destination cards or claim routes. 
  - Claim a route. If you have enough train cards of that color to claim the route (e.g four green train cards are required to claim a green  route four cars long)
     - Claiming a route awards a certain number of points depending on length
     - The train cards get placed back into the deck
     - Gray cards can be claimed by any color card, and rainbow cards can claim any route. 
     - One player cannot claim both routes in a double route
  - Draw three destination cards, and keep a minimum of one
     - If less than three destination cards, take those that are remaining. 

# When does the Game End?
- If a player has less than three cars, then each player gets one last turn and then scores are calculated

# Score Calculation
- Add or subtract the score in a destination card depending on whether it was completed by the player
- The player who has the longest continuous path gets 10 extra points with a bonus card
- Player with most points wins, and for tie breakers player with most completed destinations wins