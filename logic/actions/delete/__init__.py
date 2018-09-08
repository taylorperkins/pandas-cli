from logic.actions.base_action import BaseAction


class Delete(BaseAction):
    def __init__(self, session):
        super(Delete, self).__init__()
        self._session = session

        print(f"{self.__class__} initialized")

    def go(self):
        print(f"{self.__class__} go.")
        self._session.go()
