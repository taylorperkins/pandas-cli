import pandas as pd
from PyInquirer import prompt

from style import style

from logic.actions.base_action import BaseAction
from logic.arguments import Arguments


class Create(BaseAction):
    def __init__(self, session):
        super(Create, self).__init__()
        self._session = session

        print(f"{self.__class__} initialized")

    def go(self):
        print(f"{self.__class__} go.")

        df_name = prompt([{
            'type': 'input',
            'name': 'df_name',
            'message': 'What shall we name your dataframe?'
        }], style=style)

        df = pd.read_csv(**Arguments.go(method=pd.read_csv))

        self._session.dfs[df_name['df_name']] = df

        self._session.go()
