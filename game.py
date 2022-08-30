from Board import Board
import os
import time

def main():
    bd = Board(1)
    for i in range(5):
        bd.update()
        time.sleep(0.5)
        os.system('clear')
        


if __name__ == '__main__':
    os.system('clear')
    main()