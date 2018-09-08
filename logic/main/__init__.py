from __future__ import print_function, unicode_literals

from PyInquirer import prompt
from style import style


class Main:
    def __init__(self, session):
        self._session = session

        self._actions = {
            'create': session.create,
            'read': session.read,
            'update': session.update,
            'delete': session.delete}

        self._options = [{
            'type': 'expand',
            'name': 'action',
            'message': 'What is next?',
            'choices': [
                {
                    'key': 'c',
                    'name': 'Create DataFrame',
                    'value': 'create'
                },
                {
                    'key': 'r',
                    'name': 'Read DataFrames',
                    'value': 'read'
                },
                {
                    'key': 'u',
                    'name': 'Update DataFrame',
                    'value': 'update'
                },
                {
                    'key': 'd',
                    'name': 'Delete DataFrame',
                    'value': 'delete'
                }
            ]
        }]

    def go(self):
        print(f"{self.__class__} go.")
        print(f'Current dfs: {self._session.dfs}')
        _answers = prompt(self._options, style=style)

        print(_answers)

        self._actions[_answers['action']].go()
