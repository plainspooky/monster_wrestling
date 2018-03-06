#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Monster Wrestling
    My version in Python for the game of same name included in the book
    'WEIRD COMPUTER GAMES' from Usborne Publishing.

    https://usborne.com/browse-books/features/computer-and-coding-books/

    Copyright (C) 2017  Giovanni Nunes <giovanni.nunes@gmail.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software Foundation,
    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
"""

__author__ = 'Giovanni Nunes'
__copyright__ = "Copyright 2017, Giovanni Nunes"
__license__ = "GPL3"
__version__ = '1.0'

import curses
import gettext
import locale
from os.path import join as path_join
from random import randint, random
from time import sleep, time

BACKSPACE = 127
RETURN = 10


def init_locale():
    """Initalize localization support. Checks the current system's locale
    and tries to load it if exists. Otherwise uses the default locale.\n
    """
    locale.setlocale(locale.LC_ALL, )
    (loc, enc) = locale.getlocale()

    filename = path_join('lang', '{}.{}',
                         'LC_MESSAGES/messages.mo').format(loc, enc)

    try:
        trans = gettext.GNUTranslations(open(filename, "rb"))

    except IOError:
        trans = gettext.NullTranslations()

    trans.install()


def monster_wrestling():
    """Game based on the original "Monster Wrestling" from the WEIRD COMPUTER GAMES
    from Usborne Publishing (UK) in 1984.\n
    """

    # constants
    MAX_PANIC = 4           # number of PANIC BUTTON uses
    MAX_ROUNDS = 12         # number of rounds
    MAX_WAIT = 3.0          # wait 3s for input from keyboard

    WAIT_TIME = 1           # time to wait before begin another round

    #
    # color schemes
    #
    MONSTER = [1, 2]        # curses colors for 'round screen'
    PANIC = [3, 4]          # curses colors for 'panic button'
    ENDGAME = [5, 6]        # curses colors for 'end of game'

    #
    # change these variables to turn the game easier or hardly
    #
    distance = 3.0          # monster's distance
    max_size = 6.0          # monster's max size
    min_size = 1.0          # monster's min size

    #
    # initialize game variables and go...
    #
    panic_counter = 0       # number of panic buttons pressed
    round_counter = 0       # number of rounds
    panic = False           # normal status, no panic! no panic! no panic!
    alive = True            # you begin alive!

    # unblock getch() function
    screen.nodelay(True)

    # there are nested functions here!
    def redraw_screen(title, color):
        """(re)Draw the game screen.\n
        Clear screen and paint with the rigth colors.\n
        """
        (lines, columns) = screen.getmaxyx()

        # clear screen (repainting)
        for line in range(lines):
            try:
                screen.addstr(line, 0, b' ' * columns,
                              curses.color_pair(color[1])
                              if line == 0 else curses.color_pair(color[0]))
            except:
                pass

        # print title of this screen
        screen.addstr(0, 2, title, curses.color_pair(color[1]))

    def get_input(y, x, color, stop_time):
        """Wait user input from keyboard.\n
        """

        value = ''

        while True:
            screen.addstr(y, x, '> ' + value + ' ', curses.color_pair(color))
            key = screen.getch()

            if key == ord('p') or key == ord('P'):
                # panic button pressed! panic! panic!
                return 'PANIC'

            elif key >= ord('0') and key <= ord('9'):
                # concatenate 'value' if is a number
                value += chr(key)

            elif key == BACKSPACE:
                # remove the last character
                value = value[:-1] if len(value) > 1 else ''

            elif key == RETURN and value !='':
                # submit user's input
                return value

            if time() > stop_time:
                # exit if time is over...
                return False

    # the main loop...
    while round_counter < MAX_ROUNDS:

        # each loop is a round
        round_counter += 1

        if panic is True:

            # the PANIC mode
            panic_counter += 1

            if panic_counter > 3:
                # you blacked out!
                alive = None
                break

            # calculate values for panic mode
            oxygen_supply = randint(1, 9)
            heartbeat_increase = randint(1, 9) * oxygen_supply

            redraw_screen(_('PANIC ON!!'), PANIC)

            if panic_counter == 3:
                screen.addstr(10, 2, _(' * * * You are seeing stars * * * '),
                              curses.color_pair(PANIC[1]))

            screen.addstr(
                2, 2, _("Heartbeat increase : {}").format(heartbeat_increase),
                curses.color_pair(PANIC[0]))

            screen.addstr(4, 2, _("Oxygen supply = {}").format(oxygen_supply),
                          curses.color_pair(PANIC[0]))

            screen.addstr(6, 2, _("Amount of adrenaline?"),
                          curses.color_pair(PANIC[1]))

            # ask for adrenalin amount (be fast!)
            keyboard = get_input(7, 2, PANIC[0], time() + (MAX_WAIT / 2))

            # check keyboard input
            if keyboard == False:
                alive = False
                break
            elif keyboard != 'PANIC':
                if (oxygen_supply * int(keyboard)) == heartbeat_increase:
                    panic = False
                else:
                    alive = False
                    break

        else:
            # the MONSTER mode

            # calculate values for this round
            distance_away = int(random() * distance + distance)
            monster_size = int(random() * max_size + min_size)
            distance += 0.5
            max_size += 0.5
            min_size += 0.5

            # redraw game screen
            redraw_screen(_('Monster Wrestling'), MONSTER)

            screen.addstr(2, 2, _('Size of monster : {}').format(monster_size),
                          curses.color_pair(MONSTER[0]))

            screen.addstr(4, 2, _('Distance away : {}').format(distance_away),
                          curses.color_pair(MONSTER[0]))

            screen.addstr(6, 2, _('Muscular effort?'),
                          curses.color_pair(MONSTER[1]))

            # ask for effort!
            keyboard = get_input(7, 2, MONSTER[0], time() + MAX_WAIT)

            if keyboard == "PANIC":
                panic = True

            elif keyboard == False:
                alive = False
                break
            else:
                if (monster_size * distance_away) != int(keyboard):
                    alive = False
                    break
                else:
                    screen.addstr(2, 2, _('Monster kept at bay'),
                                  curses.color_pair(MONSTER[0]))
                    sleep(WAIT_TIME)

    screen.nodelay(False)

    redraw_screen(_('End of game!'), ENDGAME)

    if alive == True:
        messages = [
            _('Phew!!!!'),
            _('The monster is tired and has gone to look for another victim.'),
            _('You survive to tell the tale!'),
        ]
    elif alive == False:

        messages = [
            _('You have been crushed to a pulp in the monster\'s huge arms.'),
            _('You survived {} round{}.').format(round_counter,
                                                 's' if round_counter > 1 else '')
        ]
    else:
        messages = [
            _('You blacked out!'),
        ]

    position = 2

    for text in messages:
        screen.addstr(position, 2, text,
                      curses.color_pair(ENDGAME[0]))
        position += 1

    screen.addstr(6, 2, _(' Press any key to exit... '),
                  curses.color_pair(ENDGAME[1]))

    screen.getch()

    return True


def main():
    """This is the main() routine and set up the curses library.\n
    """
    curses.noecho()
    curses.start_color()

    try:
        curses.curs_set(False)
    except curses.error:
        pass

    # white foreground over blue background
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    # blue foreground over white background
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)

    # white foreground over red background
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
    # red foreground over white background
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)

    # white foreground over black background
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # black foreground over white background
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # call the game routune
    return monster_wrestling()


if __name__ == "__main__":
    init_locale()
    screen = curses.initscr()
    main()
    curses.endwin()
