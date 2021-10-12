#!/usr/bin/python3
"""
    Text indentation: Prints 2 new lines after chars:
    .,? and :
    Prototype: def text_indentation(text)
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :
    Raises:
        TypeError: text must be a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    newtext = text.replace('?', '?\n\n')
    newtext = newtext.replace('.', '.\n\n')
    newtext = newtext.replace(':', ':\n\n')

    print("\n".join([item.strip() for item in newtext.split("\n")]), end="")
