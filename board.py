import pygame


class Board:
    def __init__(self, screen: pygame.Surface, grid_size, boat_size):
        self.screen = screen
        self.grid_size = grid_size
        self.boat_size = boat_size

        # 0 -> Green -> Default square
        # 1 -> Red -> Ship hit
        # 2 -> Blue -> Ship square is here
        # 3 -> White -> Shot missed
        self.player_one_board = [
            [0 for i in range(grid_size)] for j in range(grid_size)]
        self.player_two_board = [
            [0 for i in range(grid_size)] for j in range(grid_size)]

        self.player_one_ship_coords = []
        self.player_two_ship_coords = []

        # True -> Player one board
        # False -> Player two board
        self.current_board = self.player_one_board

    def get_color(self, i, j) -> pygame.Color:
        board = self.current_board[i][j]

        if board == 0:
            return (0, 255, 0)
        elif board == 1:
            return (255, 0, 0)
        elif board == 2:
            return (0, 0, 255)
        else:
            return (255, 255, 255)

    def display_grid(self):
        size = 50
        gap = 5

        top_x = (self.screen.get_width() / 2) - ((self.grid_size / 2) * size)
        top_y = 50

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                pygame.draw.rect(self.screen, self.get_color(
                    i, j), (top_x, top_y, size, size))
                top_x += size + gap

            top_x = (self.screen.get_width() / 2) - \
                ((self.grid_size / 2) * size)
            top_y += size + gap

    def print_board(self):
        for i in self.current_board:
            for j in i:
                print(j, end=" ")
            print("")

    def place_ship(self, x1, x2, y1, y2):
        rise = abs(y2 - y1)
        current_ship_coords = self.player_one_ship_coords if self.current_board == self.player_one_board else self.player_two_ship_coords

        if rise == 0:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                current_ship_coords.append([i, y1])
                self.current_board[y1][i] = 2
        else:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                current_ship_coords.append([x1, i])
                self.current_board[i][x1] = 2
        print(self.player_one_ship_coords)

    def reset_boards(self):
        self.player_one_board = [
            [0 for i in range(self.grid_size)] for j in range(self.grid_size)]
        self.player_two_board = [
            [0 for i in range(self.grid_size)] for j in range(self.grid_size)]
