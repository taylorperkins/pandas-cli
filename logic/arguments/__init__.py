from __future__ import print_function, unicode_literals
import inspect

from PyInquirer import prompt, Separator
from style import style

from utils import show_docstring_for_method


class Arguments:
    @classmethod
    def go(cls, method):
        print(cls.__class__)

        sig_args, sig_kwargs, arg_defaults = cls._get_sig_args_and_kwargs_of_method(method)

        # Args are required, so we need user input
        if sig_args:
            return cls._get_arguments_from_user(method, sig_args, sig_kwargs, arg_defaults)
        else:
            return cls._get_arguments_from_user(method, sig_args, sig_kwargs, arg_defaults) if cls._has_arguments() else {}

    @staticmethod
    def _get_sig_args_and_kwargs_of_method(method):
        """Grabs the args and kwargs from a given method

        :param method:
        :return: tuple() --> (args, kwargs, defaults)
        """
        sig = inspect.getfullargspec(method)

        len_diff = len(sig.args) - len(sig.defaults)

        # parse out args and kwargs
        return sig.args[:len_diff], sig.args[len_diff:], sig.defaults


    @staticmethod
    def _has_arguments():
        """Determine if the user wants to specify any kwargs"""
        _answers = prompt([
            {
                'type': 'confirm',
                'name': 'has_arguments',
                'message': 'Any args?'
            }
        ], style=style)

        return _answers['has_arguments']

    @classmethod
    def _get_arguments_from_user(cls, method, sig_args, sig_kwargs, arg_defaults):
        """Given that the user wants to specify some argument values.. This method acts as the controller to do so.

        :param method: some python function
        :param sig_args: list()
        :param sig_kwargs: list()
        :return: dict() --> {arg1: ag1__value, arg2: arg2__value, ..}
        """
        # Allow the user to specify which args he wants to pass in
        chosen_kwargs = cls._select_all_kwargs(sig_args, sig_kwargs, arg_defaults)

        if 'Show Docstring' in chosen_kwargs:
            return show_docstring_for_method(method, cls._get_arguments_from_user, sig_args, sig_kwargs, arg_defaults)

        # Clean em up a bit
        final_args = sig_args + cls._clean_chosen_kwargs(chosen_kwargs)

        # Make sure the choices are not longer than 9
        cls._validate_choices(
            method=method,
            choices=final_args,
            sig_args=sig_args,
            sig_kwargs=sig_kwargs,
            arg_defaults=arg_defaults)

        # Finally return all the args and values from the user
        return cls._select_args_for_values(final_args)

    @classmethod
    def _select_all_kwargs(cls, sig_args, sig_kwargs, arg_defaults):
        """Creates a list of options for the user to choose that will ultimately be passed into a function.
        This method wraps the args in a Separator instance to serve as a disabled feature, which essentially
        requires the user to include it as a value.

        :param sig_args: list()
        :param sig_kwargs: list()
        :return: list() Args the user wants to apply to the function
        """
        # Create a list of available choices to choose from based on args and kwargs
        # Make sure to disable the args by converting to a separator
        available_choices = [{'name': 'Show Docstring'}]
        for arg in sig_args:
            available_choices.append(Separator(f'== {arg} =='))

        for ind, arg in enumerate(sig_kwargs):
            available_choices.append({'name': f'{arg} == ({arg_defaults[ind]})'})

        # Dropdown for the user to select any kwargs.
        return cls._select_kwargs_to_apply(available_choices)

    @staticmethod
    def _select_kwargs_to_apply(available_choices):
        """Basic method for displaying the available kwargs, and required args for function

        :param available_choices: list()
        :return: list()
        """
        return prompt([{
            'type': 'checkbox',
            'message': 'Select arguments available',
            'name': 'arguments',
            'choices': available_choices
        }])['arguments']

    @classmethod
    def _validate_choices(cls, method, choices, sig_args, sig_kwargs, arg_defaults):
        """The raw list method only accepts < 9 choices, so this checks for that.
        If the len is greater than 9, we start over with the args process.

        :param method: some python function
        :param choices: list()
        :param sig_args: list()
        :param sig_kwargs: list()
        :return: -
        """
        if len(choices) > 9:
            print('Sorry, but I need < 9 choices.')
            return cls._get_arguments_from_user(method, sig_args, sig_kwargs, arg_defaults)

    @staticmethod
    def _clean_chosen_kwargs(_kwargs):
        """Very much dependent on `_select_all_kwargs`
        Returns the name of the kwargs

        :param _kwargs: list()
        :return: list()
        """
        return [choice.split(' == ')[0] for choice in _kwargs]

    @staticmethod
    def _select_args_for_values(_args):
        """Final prompt to input the values for the determined args of a function based on the user's input

        :param _args:
        :return: dict() {arg1: arg1__val, arg2: arg2__val, ..}
        """
        return prompt([{
            'type': 'input',
            'name': arg,
            'message': f'{arg}:'
        } for arg in _args])
