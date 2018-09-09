import pandas as pd
from PyInquirer import prompt

from style import style

from logic.actions.base_action import BaseAction
from logic.arguments import Arguments


class Create(BaseAction):
    _AVAILABLE_EXTENSIONS = {
        'csv': pd.read_csv,
        'json': pd.read_json,
        'html': pd.read_html,
        'xls': pd.read_excel,
        'h5': pd.read_hdf,
        'feather': pd.read_feather,
        'parquet': pd.read_parquet,
        'msg': pd.read_msgpack,
        # stata
        'dta': pd.read_stata,
        # SAS
        'sas7bdat': pd.read_sas, 'xpt': pd.read_sas,
        'pkl': pd.read_pickle,
        # TODO: SQL!!!
    }

    def __init__(self, session):
        super(Create, self).__init__()
        self._session = session

        print(f"{self.__class__} initialized")

    def go(self):
        print(f"{self.__class__} go.")

        df_name = self._get_df_name()
        ext = self._get_file_extension()

        df = pd.read_csv(**Arguments.go(method=self._AVAILABLE_EXTENSIONS[ext]))

        self._session.dfs[df_name] = df

        self._session.go()

    @staticmethod
    def _get_df_name():
        """Asks the user what name to store the new dataframe under

        :return: dict() --> {'df_name': <user input>}
        """
        return prompt([{
            'type': 'input',
            'name': 'df_name',
            'message': 'What shall we name your dataframe?'
        }], style=style)['df_name']

    @classmethod
    def _get_file_extension(cls):
        """Asks the user what type of file we are reading in

        :return: dict() --> {'df_name': <user input>}
        """
        return prompt({
            'type': 'list',
            'name': 'extension',
            'message': 'What are we reading in?',
            'choices': cls._AVAILABLE_EXTENSIONS.keys()
        }, style=style)['extension']
