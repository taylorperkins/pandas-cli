from __future__ import print_function, unicode_literals
from time import sleep

from pyfiglet import Figlet

from logic.base import PandasCli


if __name__ == '__main__':
    f = Figlet(font='slant')
    print(f.renderText('pandas cli'))
    sleep(1)

    pandas_cli = PandasCli()
    pandas_cli.go()
