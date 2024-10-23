# Code goes here and DO NOT FORGET INTRO COMMENTS
import random


# Number of sticks (between 10 and 100)
def stick_count():
    Stick_count = 0
    while Stick_count < 10 or Stick_count > 100:
        print("Enter the number of sticks for the game (between 10 and 100):")
        Stick_count = int(input())
        if Stick_count < 10 or Stick_count > 100:
            print("Invalid input, please enter a number between 10 and 100.")
    return Stick_count


# Input from player
def player_move(player_name, current_Stick_count):
    print(f"{player_name}, how many sticks will you take? (1, 2, or 3):")
    move = int(input())
    while move < 1 or move > 3 or move > current_Stick_count:
        print(f"Invalid move. Please select a number between 1 and 3, and no more than {current_Stick_count} sticks.")
        move = int(input())
    return move


# Main game
def play_game(Stick_count, Player1_loss_count, Player2_loss_count, Computer_loss_count):
    current_Stick_count = Stick_count
    game_over = False

    while current_Stick_count > 1:
        # Player 1's turn
        if game_over == False:
            Player1_move = player_move("Player 1", current_Stick_count)
            current_Stick_count -= Player1_move
            print("Sticks remaining:", current_Stick_count)

            if current_Stick_count == 1:
                print("Player 1 takes the last stick and loses!")
                Player1_loss_count += 1
                game_over = True

        # Player 2's turn
        elif game_over == False:
            Player2_move = player_move("Player 2", current_Stick_count)
            current_Stick_count -= Player2_move
            print("Sticks remaining:", current_Stick_count)

            if current_Stick_count == 1:
                print("Player 2 takes the last stick and loses!")
                Player2_loss_count += 1
                game_over = True

        # Computer's turn
        elif game_over == False:
            Computer_move = random.randint(1, min(3, current_Stick_count))
            print("Computer takes", Computer_move, "stick(s).")
            current_Stick_count -= Computer_move
            print("Sticks remaining:", current_Stick_count)

            if current_Stick_count == 1:
                print("Computer takes the last stick and loses!")
                Computer_loss_count += 1
                game_over = True

    return Player1_loss_count, Player2_loss_count, Computer_loss_count


# Play again
def play_again():
    print("Do you want to play again? (yes/no):")
    response = input().lower()
    while response != "yes" and response != "no":
        print("Invalid input. Please enter 'yes' or 'no':")
        response = input().lower()
    return response == "yes"


# Main program
def main():
    print("Welcome to the Game of Sticks!")

    Player1_loss_count = 0
    Player2_loss_count = 0
    Computer_loss_count = 0
    play_more = True

    while play_more:
        Stick_count = (stick_count())
        Player1_loss_count, Player2_loss_count, Computer_loss_count = play_game(Stick_count, Player1_loss_count,
                                                                                Player2_loss_count, Computer_loss_count)
        play_more = play_again()

    # Display loss count
    print("Game over! Here are the total losses:")
    print("Player 1:", Player1_loss_count, "losses")
    print("Player 2:", Player2_loss_count, "losses")
    print("Computer:", Computer_loss_count, "losses")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
