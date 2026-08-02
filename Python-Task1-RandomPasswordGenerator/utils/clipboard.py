import pyperclip


def copy(password):

    if password:
        pyperclip.copy(password)