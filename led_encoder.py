from pyfirmata import ArduinoDue
from pyfirmata import util

board = ArduinoDue('COM3')
LEDS = [board.get_pin('d:3:o'), board.get_pin('d:5:o'), board.get_pin('d:6:o'), board.get_pin('d:9:o')]
SW = board.get_pin('d:10:i')

it = util.Iterator(board)
it.start()


def encode(num):
    if num < 0:
        num = 0
    elif num >= 16:
        num = 15

    str = '{0:04b}'.format(num)

    for i, value in enumerate(str):
        LEDS[i].write(int(value))

    return str


def read_sw():
    return str(SW.read())
