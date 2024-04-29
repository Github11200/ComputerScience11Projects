# Example file showing a basic pygame "game loop"
import pygame

from board import Board
from utils import PygameUtils

# pygame setup
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame_utils = PygameUtils(screen=screen)
board = Board(screen=screen, grid_size=10, boat_size=5)

# [2, 5, 2, 3] -> (2, 5), (2, 3)
boat_coords_player_one = [-1, -1, -1, -1]
boat_coords_player_two = [-1, -1, -1, -1]
boat_coords_i = 0
coords_recorded = False
start_game = False

# True -> Player 1
# False -> Player 2
player_one_playing = True
coords = []


def display_player_coordinates_inputs(pygame_utils, boat_coords_player_one, boat_coords_player_two):
    coords_to_display = boat_coords_player_one if boat_coords_player_one[
        3] == -1 else boat_coords_player_two
    pygame_utils.display_text(
        f"({coords_to_display[0]}, {coords_to_display[1]}), ({coords_to_display[2]}, {coords_to_display[3]})", 22, (0, 0, 0), 690)


def get_key_pressed_by_converting_from_number_to_ascii(key_pressed):
    return int(chr(
        key_pressed[0] + (19 if key_pressed[0] < 39 else 9)))


def should_switch_to_different_player(boat_coords_player_two, boat_coords_i):
    return boat_coords_i + 1 == 4 and boat_coords_player_two[0] == -1


def display_new_board_data():
    board.display_grid()
    pygame.display.flip()
    pygame.time.delay(2000)


def get_what_key_is_pressed_based_on_what_value_from_the_array_is_true(keys):
    return [i for i, val in enumerate(keys) if val]


def player_two_board_coordinates_recorded(boat_coords_player_two):
    return boat_coords_player_two[3] == -1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # TODO: Fix the board so that inputting 1115 and 1511 both work
    if not coords_recorded:
        pygame_utils.display_text(
            f"Player {1 if boat_coords_player_one[3] == -1 else 2}, please press enter 4 numbers for the 2 coordinates of your boat of size {board.boat_size} (eg. 2325 will make the coordinates be (2, 3)and (2, 5)),", 20, (0, 0, 0))

        pygame_utils.display_text(
            f"the numbers will be displayed below, and when all the numbers have been entered the ship will be shown on the board for 2 seconds. YOU CAN ONLY ENTER A SINGLE DIGIT NUMBER AND IT IS 0 INDEXED.", 20, (0, 0, 0), 670)

        display_player_coordinates_inputs(
            pygame_utils, boat_coords_player_one, boat_coords_player_two)

        keys = pygame.key.get_pressed()
        key_pressed = get_what_key_is_pressed_based_on_what_value_from_the_array_is_true(
            keys)

        if key_pressed and boat_coords_i < len(boat_coords_player_one):
            number = get_key_pressed_by_converting_from_number_to_ascii(
                key_pressed)

            # Update either the player one or two's coordinates based on which one doesn't have it yet
            if boat_coords_player_one[3] == -1:
                boat_coords_player_one[boat_coords_i] = number
            else:
                boat_coords_player_two[boat_coords_i] = number

            if should_switch_to_different_player(boat_coords_player_two, boat_coords_i):
                board.place_ship(
                    boat_coords_player_one[0], boat_coords_player_one[2], boat_coords_player_one[1], boat_coords_player_one[3])

                display_new_board_data()

                boat_coords_i = 0
                board.current_board = board.player_two_board
            else:
                boat_coords_i += 1
            pygame.time.wait(200)
        elif not player_two_board_coordinates_recorded(boat_coords_player_two):
            board.place_ship(
                boat_coords_player_two[0], boat_coords_player_two[2], boat_coords_player_two[1], boat_coords_player_two[3])

            display_new_board_data()

            board.reset_boards()

            # Change the current board to player one's board
            board.current_board = board.player_one_board

            # All the coordinates for both player's ships have been recorded
            coords_recorded = True

            # Start the actual game now that the boards are setup
            start_game = True
    elif start_game:
        pygame_utils.display_text(
            f"PLAYER {1 if player_one_playing else 2}: Enter the two coordinates at which you want to shoot. Inputting the numbers 2, 3 will shoot at (2, 3), all the coordinates are also 0 indexed", 20, (0, 0, 0))

        pygame_utils.display_text(
            f"({-1 if len(coords) == 0 else coords[0]}, {-1 if len(coords) < 2 else coords[1]})", 20, (0, 0, 0), 670)

        if len(coords) < 2:
            keys = pygame.key.get_pressed()
            key_pressed = get_what_key_is_pressed_based_on_what_value_from_the_array_is_true(
                keys)
            if key_pressed:
                number = get_key_pressed_by_converting_from_number_to_ascii(
                    key_pressed)
                coords.append(number)
                print(coords)
            pygame.time.wait(200)
        else:
            current_player_ship_coords = board.player_one_ship_coords if not player_one_playing else board.player_two_ship_coords
            if coords in current_player_ship_coords:
                board.current_board[coords[1]][coords[0]] = 1
                current_player_ship_coords.remove(coords)
                display_new_board_data()

                if len(current_player_ship_coords) == 0:
                    pygame_utils.display_text(
                        f"GAME OVER: PLAYER {1 if player_one_playing else 2} HAS WON!!!!!", 20, (0, 0, 0), 700)
                    pygame.display.flip()
                    pygame.time.wait(1500)
                    running = False
                else:
                    pygame.time.wait(1500)
                coords.clear()

                board.current_board = board.player_one_board if not player_one_playing else board.player_two_board
                player_one_playing = not player_one_playing
            else:
                board.current_board[coords[1]][coords[0]] = 3
                display_new_board_data()
                pygame.time.wait(1500)
                coords.clear()
                board.current_board = board.player_one_board if not player_one_playing else board.player_two_board
                player_one_playing = not player_one_playing

    # RENDER YOUR GAME HERE
    board.display_grid()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
