# Author: Darren Cruz
# email: darrenjcruz@gmail.com

'''
This module contains the ConnectFour console which is what runs the game.
'''

import connectfour

def main():
    game = connectfour.ConnectFour()
    game.menu()

if __name__ == '__main__':
    main()
