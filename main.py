import os
from classes.map import Map
from classes.player import Player
from classes.room import Room


def main():
    game_loop()
    return None


def setup():
    game_map = Map('First', (3, 3))

    rooms = os.listdir(r'rooms')
    for room in rooms:
        with open(room, 'r') as fp:
            content = fp.read()

    player_init_position = 0, 0

    player = Player(where=game_map)

    player.set_position(player_init_position)

    return player


def game_loop():
    player = setup()

    running = True

    while running:
        command = input('> ').strip().lower()
        match command.split():
            case ['exit']:
                running = False

            case['go', ('north' | 'south' | 'east' | 'west') as direction]:
                player.move_char(direction)

            case _:
                print(command)
                print('Invalid command. Try again.')


if __name__ == '__main__':
    main()

