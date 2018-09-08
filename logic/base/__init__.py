from logic.main import Main

from logic.actions.create import Create
from logic.actions.read import Read
from logic.actions.update import Update
from logic.actions.delete import Delete


class PandasCli:
    def __init__(self):
        print(f'{self.__class__} initialized')

        self.dfs = {}

        self.create = Create(session=self)
        self.read = Read(session=self)
        self.update = Update(session=self)
        self.delete = Delete(session=self)

        # This needs to be after CRUD
        self.main = Main(session=self)

    def go(self):
        print(f'{self.__class__} go')
        self.main.go()
