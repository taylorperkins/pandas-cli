from __future__ import print_function, unicode_literals

from logic.actions.base_action import BaseAction


class Read(BaseAction):
    def __init__(self, session):
        super(Read, self).__init__()
        self._session = session

        print(f"{self.__class__} initialized")

    def go(self):
        print(f"{self.__class__} go.")
        self._session.go()
