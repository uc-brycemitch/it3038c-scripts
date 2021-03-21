"""Simulating the dice game Craps using graphs.
Solution uses Figure 5.2 code from Intro to Python for Data Science by Dietel as a base.
This base code is located here: https://github.com/pdeitel/IntroToPython/blob/master/examples/ch04/fig04_02.py"""
import random       # Used to generate random numbers for dice rolls.
import statistics   # Used to calculate mean, median, and mode.
import sys          # Used to get user's argument for number of games to simulate.

# Make sure user entered an int as an argument.
try:
    # Number of games of craps to simulate.
    number_of_simulations = int(sys.argv[1])
except:
    # User failed to provide an int.
    print("ERROR: Your argument is either empty or not an int. Exiting.")
    # Exit with error code 1 to help with debugging.
    exit(1)

# Make sure user provides a positive int.
if number_of_simulations < 1:
    print("ERROR: I can't do 0 or negative simulations :P. Provide me with a positive int. Exiting.")
    # Exit with error code 2 to help with debugging.
    exit(2)

# User provided "gui" argument, user wants to display GUI graphs. Attempt to import modules needed to do this.
importSuccessful = 0 # Used to keep track of whether import of modules needed to display GUI graphs was successful.
if len(sys.argv) == 3 and sys.argv[2].lower() == "gui":
    try:
        import matplotlib.pyplot as plt # Necessary to draw graphs
        import pandas as pd             # Used to draw graphs in a grouped manner
        importSuccessful = 1            # Import was successful
    except:
        print("Unable to import modules needed to display GUI graphs. Will not be displaying them even though they were requested with gui argument.")
        print("You need to install matplotlib and pandas modules from pip to be able to do this. Refer to the README for more information.\n")


# Define two lists to track the total numbers of games won and lost on the first roll, second roll, third roll and so on.
# A win or loss within the first 12 rolls are tracked exactly, a win or loss after 12+ rolls is summed into one number.
# Meaning a win on roll 1, leads to win_frequency[0]++.
# And a loss on roll 7, leads to loss_frequency[8]++.
# And a loss on roll 13 or 39 or 56 or any roll after 12, leads to loss_frequency[12]++.
win_frequency = [0] * 13
loss_frequency = [0] * 13

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def play_craps(number_of_games):
    """Play a game of craps."""
    for i in range(number_of_games):
        # Keep track of number of rolls till a win or loss occurs.
        number_of_rolls = 0

        die_values = roll_dice()  # first roll
        number_of_rolls += 1

        # determine game status and point, based on first roll
        sum_of_dice = sum(die_values)
        if sum_of_dice in (7, 11):  # win
            game_status = 'WON'
        elif sum_of_dice in (2, 3, 12):  # lose
            game_status = 'LOST'
        else:  # remember point
            game_status = 'CONTINUE'
            my_point = sum_of_dice

        # continue rolling until player wins or loses
        while game_status == 'CONTINUE':
            die_values = roll_dice()
            number_of_rolls += 1
            sum_of_dice = sum(die_values)

            if sum_of_dice == my_point:  # win by making point
                game_status = 'WON'
            elif sum_of_dice == 7:  # lose by rolling 7
                game_status = 'LOST'

        # Change number of rolls to 13 if it took more than that to get to a win/loss.
        # This is because we sum all wins/losses after 12 rolls into one number.
        if number_of_rolls > 13:
            number_of_rolls = 13

        # Keep track of win or loss
        if game_status == 'WON':
            win_frequency[number_of_rolls - 1] += 1
        else:
            loss_frequency[number_of_rolls - 1] += 1

try:
    play_craps(number_of_simulations)

    # Store some data used to display some stats later
    games_won = sum(win_frequency) # Number of games won
    games_lost = sum(loss_frequency) # Number of games lost
    total_frequency = [win + loss for win, loss in zip(win_frequency, loss_frequency)] # List with total games (wins+losses) at each number of rolls.
    games_total = sum(total_frequency) # Total number of games played, should equal number_of_simulations.

    # Make sure number of games played equals number of simulations requested, just to be safe.
    if games_total != number_of_simulations:
        print('ERROR: games_total does not match number_of_simulations. Exiting.')
        # Exit with error code 3 to help with debugging.
        exit(3)

    # Determine probability of winning craps from games simulated
    probability_of_winning = games_won / games_total

    # Expand total_frequency list into a list that has a value for each occurrence.
    # Meaning if total_frequency[0] = 7, then total_frequency_value will have the values [1, 1, 1, 1, 1, 1, 1] to start with.
    # And if total_frequency[12] = 5, then total_frequency_value will have the values [13, 13, 13, 13, 13, 13, 13] also.
    # This is done to make it easy to calculate measures of central tendency, especially median, later.
    total_frequency_expanded = (
        total_frequency[0] * [1] +
        total_frequency[1] * [2] +
        total_frequency[2] * [3] +
        total_frequency[3] * [4] +
        total_frequency[4] * [5] +
        total_frequency[5] * [6] +
        total_frequency[6] * [7] +
        total_frequency[7] * [8] +
        total_frequency[8] * [9] +
        total_frequency[9] * [10] +
        total_frequency[10] * [11] +
        total_frequency[11] * [12] +
        total_frequency[12] * [13]
    )

    # Calculate mean, median, and mode using statistics module.
    mean = statistics.mean(total_frequency_expanded)
    median = statistics.median(total_frequency_expanded)
    mode = statistics.mode(total_frequency_expanded)

    # Print various stats from games simulated
    print(f'Following statistics calculated from {games_total:,} craps games.')    # Total games
    print(f'Number of winning dice rolls: {sum(win_frequency):,}.')                # Number of wins
    print(f'Number of losing dice rolls: {sum(loss_frequency):,}.')                # Number of losses
    print(f'Probability of winning: {probability_of_winning:,}.')                  # Probability of winning
    print(f'Mean of number of dice rolls before a game ends: {mean:,}.')           # Mean
    print(f'Median of number of dice rolls before a game ends: {median:,}.')       # Median
    print(f'Mode of number of dice rolls before a game ends: {mode:,}.')           # Mode

    # If user wants to display GUI graphs and modules to do so were imported successfully, then display GUI graphs
    # Plot lists of wins and losses in a horizontal grouped bar graph.
    # Plotted using pandas module. Reference: https://stackoverflow.com/a/56177691
    if importSuccessful:
        print("\nDisplaying data of craps graphs in GUI...")
        # y-axis data point labels
        index = [item for item in range(1, 13)]
        # Value of index[] is now [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, '13+']
        index += ['13+']
        # Store win & loss data grouped by index
        data_frame = pd.DataFrame({'Number of Wins': win_frequency, 'Number of Losses': loss_frequency}, index=index)
        # Plot data on graph as horizontal bar graph
        axes = data_frame.plot.barh()
        # Label the axes of graph
        axes.set(xlabel='Win/Loss Frequency', ylabel='Number of Die Rolls')
        # Label the title of graph
        axes.set_title(f'Win/Loss Frequency by Number of Dice Rolls for {number_of_simulations:,} Craps Games')
        # Display the graph
        plt.show()

except:
    # Something has gone wrong, not sure what since user input is validated with another try statement above.
    print("ERROR: Something went wrong! Exiting.")
    # Exit with error code 4 to help with debugging.
    exit(4)

# Cleanly exit the program.
exit(0)