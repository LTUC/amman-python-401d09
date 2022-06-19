class Game:
    def __init__(self):
        self.remaining_dice = 6
        self.bank = Banker()
        self.user_input = ''
        self.round_num = 1

    def play(self, roller = GameLogic.roller):
        pass
    # Print Welcome Message
    # Ask the user if he/she want to play --> Check the user input if yes or no

    # function Round()
    # function Quit()
    # function Bank()
    # function Rolling()
    # print the round number
    # rolling Dice (print the number of dice and show the dice)
    # Check if it is Zilch
    # Check if it is a hot dice
        # Hot Dice:
            # Add the points to shelf
            # Reset the the remaining dice
            # Rolling
    # Ask the user for keeping dice or quit (if quit end the game and print thanking message)
    # If not quit, check if it is cheating calculate the score and add that to shelf
    # and subtract the number of dice from the total number of dice
    # Print the unbanked points with the remaining dice
    # Ask the user (r)oll again, (b)ank your points or (q)uit:
        # Quit:
            # end the game and print thanking message

        # Banking:
            # Print the banked points and the number of the round
            # Print the total score
            # Reset the number of dice to 6
            # Reset the unbank points to 0
            # increase the number of the round

        # Rolling:
            # Print the remaining dice
            # Print the dice
            # Ask the user for keeping dice or quit (if quit end the game and print thanking message)
            # If not quit calculate the score and add that to shelf
            # and subtract the number of dice from the total number of dice
            # Print the unbanked points with the remaining dice
            # Ask the user (r)oll again, (b)ank your points or (q)uit:
    # start new Round

# 1,1,2,3,5,4
# > 1,1,5
# 1,5,6
# > 1,5
# 1

# 2,2,4,6
