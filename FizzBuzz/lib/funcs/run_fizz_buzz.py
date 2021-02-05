#! /usr/bin/env python3


def run_fizz_buzz(
    num, fizzes_and_buzzes, separator="", sort_divisors=True, sort_words=True
):
    """General FizzBuzz function for a list of FizzBuss objects.

    For each object, we return the word associated to the divisor, d, if the
    input number is divisible.

    We allow the fizzes_and_buzzes list to be sorted from smallest divisor to largest divisor.

    Args:
        num (int): the number we want to divide
        fizzes_and_buzzes (list): list of FizzBuzz objects
        separator (str): the string separating the words
        sort_divisor (bool): sort the divisors from smallest to largest
        sort_words (bool): sort the the words alphabetically. Note sort_divisor
        takes precendece, so if both are True, we sort by divisor.

    Returns:
        string (str): a string of the results of the FizzBuzz test.
    """

    if sort_divisors:
        fizzes_and_buzzes.sort(key=lambda x: x.div)

    elif sort_words:
        fizzes_and_buzzes.sort(key=lambda x: x.word)

    string = separator.join([fb.word for fb in fizzes_and_buzzes if not (num % fb.div)])

    if string:
        return string
    else:
        return num
