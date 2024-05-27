#!/usr/bin/python3
def multiple_returns(sentence):
    """
    a function that returns a tuple with the length of
    a string and its first character.
    """
    if len(sentence) == 0:
        sentence = None
        tuple_output = (0, sentence)
        return tuple_output
    else:
        count = len(sentence)
        tuple_output = (count, sentence[0])
        return tuple_output
