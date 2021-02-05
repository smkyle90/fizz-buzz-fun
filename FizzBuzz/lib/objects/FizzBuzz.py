#! /usr/bin/env python3

class FizzBuzz:
    def __init__(self, word, div):
        """A FizzBuzz class that associated a divisor
        with a word for the FizzBuzz problem.

        Args:
            word (str): a string
            div (int): an integer that acts as the divisor in the FizzBuzz problem

        """
        self.word = word
        self.div = div

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, word):
        if isinstance(word, str):
            self.__word = word
        else:
            raise TypeError("Word must be of type string.")

    @property
    def div(self):
        return self.__div

    @div.setter
    def div(self, div):

        if isinstance(div, int) and (div > 0):
            self.__div = div
        else:
            raise TypeError("Divisor must be of type int and be greater than zero.")

    def __repr__(self):
        return "Word: {}. Divisor: {}".format(self.word, self.div)