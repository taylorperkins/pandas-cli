from __future__ import print_function, unicode_literals
import sys
from time import sleep

from pyfiglet import Figlet

from logic.main import NoAnswersError
from logic.base import PandasCli


if __name__ == '__main__':
    f = Figlet(font='slant')
    print(f.renderText('pandas cli'))
    sleep(1)

    try:
        pandas_cli = PandasCli()
        pandas_cli.go()

    except (NoAnswersError, Exception) as e:
        print(e.with_traceback)
        print('Bye!')
        sys.exit()
