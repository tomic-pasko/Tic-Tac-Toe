import random
from ascii_art import title
from board import Playground

numbers_to_pick = [1, 2, 3, 4, 5, 6, 7, 8, 9]
picked_numbers = []

# Until all numbers are picked from number
# To Do - Make grid, maybe list of characters, eg. ['- | - | -', '- - - - -', '- | - | -', '- - - - -', '- | - | -']
# To Do - Print "x" or "o" on chosen spot in grid
# Make list of winning combinations, eg. 123, 456, 789, 159...

print(f'{title}')
print('### Two player game! ###')

playground = Playground()
playground.draw_grid()
x = False
game_on = True
picked_numbers_by_x = []
picked_numbers_by_o = []
result_x = []
result_o = []

winning_combo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

while game_on:
    # Toggle player1 ('x') and player2 ('o')
    x = not x
    try:
        if x:
            picked_number = int(input(f"Player 1 Choose a space inside grid, eg. 1-9:"))
        else:
            picked_number = int(input(f"Player 2 Choose a space inside grid, eg. 1-9:"))
    except ValueError:
        print("Please enter a number.")
        x = not x
    else:
        if picked_number in picked_numbers:
            print("Please choose number that is still available.")
            print(f"Available numbers are: {numbers_to_pick}")
        else:
            if 1 <= picked_number <= 9:
                if x:
                    picked_numbers_by_x.append(picked_number)
                else:
                    picked_numbers_by_o.append(picked_number)
                numbers_to_pick.remove(picked_number)

                # call method to refresh grid
                playground.refresh_grid(str(picked_number), x)
                playground.draw_grid()
            else:
                print("Please choose whole number between 1 and 9.")

    # Checking for winner and finishing the game
    for i in winning_combo:
        result_x.append(all(elem in picked_numbers_by_x for elem in i))
        result_o.append(all(elem in picked_numbers_by_o for elem in i))

    if any(result_x):
        game_on = False
        print("Player 1 wins!")
    elif any(result_o):
        game_on = False
        print("Player 2 wins!")
    elif len(numbers_to_pick) < 1:
        game_on = False
        print("Draw!")
    else:
        game_on = True

# TO DO: Game for one player, and smart algorithm, so computer prevents player from winning
