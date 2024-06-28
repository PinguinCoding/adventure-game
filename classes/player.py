class Player(object):
    def __init__(self, where):
        self.position = None
        self.where = where

    def set_position(self, new_position: tuple):
        try:
            self.where.matriz[self.position]

        except IndexError:
            return print("You can't go that way")

        else:
            self.position = new_position
            self.get_position()

    def get_position(self):
        print('Player object at {}, on (x: {}, y: {})'.format(self.where.name, *self.position))
        return None

    def move_char(self, direction: str):
        match direction:
            case 'north':
                x, y = self.position
                self.set_position((x, y+1))
            case 'south':
                x, y = self.position
                self.set_position((x, y-1))
            case 'west':
                x, y = self.position
                self.set_position((x-1, y))
            case 'east':
                x, y = self.position
                self.set_position((x+1, y))
