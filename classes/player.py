from collections import namedtuple


class Player(object):
    def __init__(self, where):
        self.position = namedtuple('Position', ['x', 'y'])
        self.current_position = None
        self.where = where

    def set_position(self, new_position: tuple):
        if new_position[0] < 0 or new_position[1] < 0:
            return print("You can't go that way")
        elif new_position[0] > len(self.where.matriz)-1 or new_position[1] > len(self.where.matriz)-1:
            return print("You can't go that way")
        else:
            self.current_position = self.position(*new_position)
            self.show_position()

    def show_position(self):
        print(self.current_position)
        return None

    def move_char(self, direction: str):
        match direction:
            case 'north':
                x, y = self.current_position
                self.set_position((x, y+1))
            case 'south':
                x, y = self.current_position
                self.set_position((x, y-1))
            case 'west':
                x, y = self.current_position
                self.set_position((x-1, y))
            case 'east':
                x, y = self.current_position
                self.set_position((x+1, y))
