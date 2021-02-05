#! /usr/bin/env python3

from lib.objects import FizzBuzz
from lib.funcs import run_fizz_buzz

if __name__ == "__main__":
    fb_list = [
        FizzBuzz("Fizz", 3),
        FizzBuzz("Buzz", 5),
        FizzBuzz("Ducky", 2),
        FizzBuzz("Fuzz", 6),
    ]

    for i in range(1, 22):
        print(i, run_fizz_buzz(i, fb_list))
