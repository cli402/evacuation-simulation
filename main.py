'''
 main.py

 author: Daniel Henderson
'''

import grid_info
import ui_module


def main():
    UI = ui_module.UserInterface(grid_info.grid_size, grid_info.tile_size, 'tech_square.jpg')

    while not UI.checkEvents():
        UI.drawScreen(grid_info.update_grid())
    UI.quit()


if __name__ == '__main__':
    main()