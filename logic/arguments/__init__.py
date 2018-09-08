from __future__ import print_function, unicode_literals
import inspect

from PyInquirer import prompt
from style import style


class Arguments:
    @classmethod
    def go(cls, method):
        print(cls.__class__)
        return cls._get_arguments(method) if cls._has_arguments() else {}

    @staticmethod
    def _has_arguments():
        _answers = prompt([
            {
                'type': 'confirm',
                'name': 'has_arguments',
                'message': 'Any args?'
            }
        ], style=style)

        return _answers['has_arguments']

    @classmethod
    def _get_arguments(cls, method):
        sig = inspect.getfullargspec(method)
        choices = [
            {'name': f'{arg} == ({sig.defaults[ind] if ind < len(sig.defaults) else ""})'}
            for ind, arg in enumerate(sig.args)]

        arg_choices = cls._validate_choices(
            method,
            choices=prompt([{
                'type': 'checkbox',
                'message': 'Select arguments available',
                'name': 'arguments',
                'choices': choices
            }]))

        kwargs = prompt(cls._clean_chosen_arguments(arg_choices), style=style)

        print(kwargs)

        return kwargs

    @classmethod
    def _validate_choices(cls, method, choices):
        """The raw list method only accepts < 9 choices.

        :param method:
        :param choices:
        :return:
        """
        if len(choices) > 9:
            print('Sorry, but I need < 9 choices.')
            return cls._get_arguments(method)
        else:
            return choices

    @staticmethod
    def _clean_chosen_arguments(choices):
        choices = [choice.split(' == ')[0] for choice in choices['arguments']]

        return [{
            'type': 'input',
            'name': choice,
            'message': f'{choice}: '
        } for choice in choices]
