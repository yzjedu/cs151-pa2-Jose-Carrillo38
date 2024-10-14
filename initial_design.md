# Algorithm

Start the game by prompting the user to choose the number of sticks for the game (between 10 and 100).

If the user enters a number outside the range, ask again until a valid number is provided.
Assign three players: two human players (Player 1 and 2) and one computer. Set each player's loss count to zero.

While the number of sticks remaining is more than one:

Player 1's turn: Prompt Player 1 to take 1, 2, or 3 sticks.
If Player 1 inputs a number outside 1-3 or greater than remaining sticks, Prompt player again.
Subtract the number of sticks Player 1 took from the total and display how many are left.

Player 2's turn: Prompt Player 2 to take 1, 2, or 3 sticks.
If Player 2 inputs a number outside 1-3 or greater than remaining sticks, Prompt player again.
Subtract the number of sticks Player 2 took from the total and display how many are left.

Computer's turn: It Randomly selects 1, 2, or 3 sticks.
Ensure the computer’s choice does not exceed the remaining sticks.
Subtract the sticks the computer took and display its choice and how many are left.

When only one stick remains, the player forced to take it loses or wins

Display the player who took the last stick as the loser and increase their loss count by one. 
Display the loss count for each player.

Prompt the players if they want to play again.

If the input is anything other than "yes" or "no", prompt them to answer again.
If yes, restart the game by asking for the new number of sticks and continue playing, keeping track of losses.
If no, end the game and display the total number of losses for each player across all games.

# Coding this is going to be difficult. How would I make the computer player smarter? 
# What if the player says no, but then changed his mind. The thought crossed my mind but I have no idea how to adjust to that
# I'm using what's on line 8 to keep the game going but I don't know if that's right

