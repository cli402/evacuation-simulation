'''
 main.py

 author: Daniel Henderson
'''

import generator
import grid_info
import ui_module
import threading
import Queue


def main():
    agent_queue = Queue.Queue()
    UI = ui_module.UserInterface(grid_info.grid_size, grid_info.tile_size, 'tech_square.jpg')
    Gen = generator.Generator(agent_queue, grid_info.x_range, grid_info.y_range)

    # start generator thread
    gen_thread = threading.Thread(target=Gen.mainLoop)
    gen_thread.daemon = True
    gen_thread.start()

    while not UI.checkEvents():
        coordinates = agent_queue.get()
        UI.drawScreen(coordinates)
    UI.quit()


if __name__ == '__main__':
    main()
