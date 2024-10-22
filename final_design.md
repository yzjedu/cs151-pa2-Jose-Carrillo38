# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 

Start the game by prompting the user to choose the number of sticks for the game (between 10 and 100).

While user enters a number outside the range:
    Ask again until a valid number is provided.

Assign three players: two human players (Player 1 and Player 2) and one computer.
Set each player's loss count to zero.

While the number of sticks remaining is more than one:

    Player 1's turn:
        Prompt Player 1 to take 1, 2, or 3 sticks.
        If Player 1 inputs a number outside 1-3 or greater than remaining sticks:
            Prompt player again until a valid input is given.
        Subtract the number of sticks Player 1 took from the total.
        Display how many sticks are left.

    Player 2's turn:
        Prompt Player 2 to take 1, 2, or 3 sticks.
        If Player 2 inputs a number outside 1-3 or greater than remaining sticks:
            Prompt player again until a valid input is given.
        Subtract the number of sticks Player 2 took from the total.
        Display how many sticks are left.

    Computer's turn:
        Randomly select 1, 2, or 3 sticks.
        Ensure the computer’s choice does not exceed the remaining sticks.
        Subtract the sticks the computer took from the total.
        Display the computer's choice and how many sticks are left.

When only one stick remains:
    The player forced to take the last stick loses.
    Increase their loss count by one.
    Display the player who took the last stick as the loser.
    Display the loss count for each player.

Prompt the players if they want to play again:
    If the input is anything other than "yes" or "no":
        Prompt them to answer again.

    If yes:
        Restart the game by asking for the new number of sticks.
        Continue playing, keeping track of losses.

    If no:
        End the game.
        Display the total number of losses for each player across all games.
