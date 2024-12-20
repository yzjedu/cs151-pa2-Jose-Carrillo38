# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 

Start the game by prompting the user to choose the number of sticks for the game (between 10 and 100).

While user enters a number outside the range:
    Display "Invalid input, please enter a number between 10 and 100."
    Ask again until a valid number is provided.

Assign three players: two human players (Player 1 and Player 2) and one computer.
Set each player's loss count to zero.

While the number of sticks remaining is more than one:
    
    Player 1's turn:
        Prompt Player 1 to take 1, 2, or 3 sticks.
        If Player 1 inputs a number outside 1-3 or greater than the remaining sticks:
            Display "Invalid move. Please select a number between 1 and 3, and no more than remaining sticks."
            Prompt Player 1 again until valid input is provided.
        Once a valid input is received:
            Subtract the number of sticks Player 1 took from the total.
            Display how many sticks are left.

    Player 2's turn:
        Prompt Player 2 to take 1, 2, or 3 sticks.
        If Player 2 inputs a number outside 1-3 or greater than the remaining sticks:
            Display "Invalid move. Please select a number between 1 and 3, and no more than remaining sticks."
            Prompt Player 2 again until valid input is provided.
        Once a valid input is received:
            Subtract the number of sticks Player 2 took from the total.
            Display how many sticks are left.

    Computer's turn:
        Randomly select 1, 2, or 3 sticks.
        Ensure the computer’s choice does not exceed the remaining sticks.
        If the computer’s random selection exceeds the remaining sticks:
            Re-select a valid number (1-3 sticks).
        Once a valid choice is made:
            Subtract the sticks the computer took from the total.
            Display the computer's choice and how many sticks are left.

When only one stick remains:
    The player forced to take the last stick loses.
    Display "Player X loses the game for taking the last stick."
    Increase their loss count by one.
    Display the updated loss count for each player.

Prompt the players if they want to play again:
    If the input is anything other than "yes" or "no":
        Display "Please enter 'yes' to continue or 'no' to quit."
        Ask again until a valid response is given.

    If the response is "yes":
        Restart the game by asking for the new number of sticks.
        Continue playing, keeping track of losses.

    If the response is "no":
        End the game.
        Display the total number of losses for each player across all games.
        Say goodbye.

# Prompt the user to select the number of sticks. If the user inputs an invalid number, such as a number outside the range of 10 to 100, it’s considered wrong and they are asked to input again. This ensures that the game starts with a valid number of sticks.
# At the end of the game, players are prompted if they want to play again. If the response is anything other than "yes" or "no", it is considered wrong, and the program keeps prompting for a valid input to ensure a clear next step.
# Each player (Player 1, Player 2, and Computer) is asked to select 1-3 sticks. If a player chooses an invalid number (e.g., a number outside 1-3 or greater than the remaining sticks), it’s wrong, and they are prompted again until they provide a valid input. This ensures fair play and keeps the game within the rules.
