import random

from pyboy import PyBoy
from pyboy.utils import WindowEvent


# Action map
action_map = {
    "Left": [WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT],
    "Right": [WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT],
    "Down": [WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN],
    "A": [WindowEvent.PRESS_BUTTON_A, WindowEvent.RELEASE_BUTTON_A],
}

start_y = 24


def turn_block(pyboy):
    pyboy.send_input(action_map["A"][0])
    pyboy.tick()
    pyboy.send_input(action_map["A"][1])
    pyboy.tick()


def move_block_sideways(pyboy, action: str):
    pyboy.send_input(action_map[action][0])
    pyboy.tick()
    pyboy.send_input(action_map[action][1])
    pyboy.tick()


def move_block_down(pyboy):
    pyboy.send_input(action_map["Down"][0])
    pyboy.tick()
    pyboy.send_input(action_map["Down"][1])


def spawn_pyboy(show=True):
    window = "SDL2" if show else "null"
    pyboy = PyBoy(r"C:\Users\Admin\Downloads\Tetris\Tetris.gb", window=window)
    # pyboy.set_emulation_speed(0)
    tetris = pyboy.game_wrapper
    tetris.start_game()
    # Set block animation to fall instantly
    # pyboy.memory[0xFF9A] = 2
    return pyboy, tetris


def get_current_block_text(block_tile):
    if 0 <= block_tile <= 3:
        return "L"
    elif 4 <= block_tile <= 7:
        return "J"
    elif 8 <= block_tile <= 11:
        return "I"
    elif 12 <= block_tile <= 15:
        return "O"
    elif 16 <= block_tile <= 19:
        return "Z"
    elif 20 <= block_tile <= 23:
        return "S"
    elif 24 <= block_tile <= 27:
        return "T"


def example_play():
    pyboy, tetris = spawn_pyboy()
    run = 0
    while run < 10:
        move = random.choice(list(action_map.keys()))

        pyboy.send_input(action_map[move][0])
        pyboy.tick()
        pyboy.send_input(action_map[move][1])
        pyboy.tick()
        if tetris.game_over():
            tetris.reset_game()
            run += 1


if __name__ == "__main__":
    example_play()
