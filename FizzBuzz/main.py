#! /usr/bin/env python3

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from .lib.funcs import run_fizz_buzz
from .lib.objects import FizzBuzz

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/execute", methods=["POST"])
def execute():
    request_dict = request.form.to_dict()

    fb_data = [(k, int(v.strip("/"))) for k, v in request_dict.items() if "fb" not in k]
    fb_list = [FizzBuzz(*fb) for fb in fb_data]

    # Extract parameters from form
    number = request_dict["fbNumber"]
    separator = str(request_dict["fbSeparator"])

    if number:
        num_range = [int(number)]
        num_show = number
    else:
        num_range = [i + 1 for i in range(100)]
        num_show = "1 to 100"

    sort_numeric = False
    sort_alphabetic = False

    if "fbSortNumeric" in request_dict:
        if request_dict["fbSortNumeric"] == "on":
            sort_numeric = True
    elif "fbSortAlphabetical" in request_dict:
        if request_dict["fbSortAlphabetical"] == "on":
            sort_alphabetic = True

    try:
        result = [
            (
                number,
                run_fizz_buzz(
                    number, fb_list, separator, sort_numeric, sort_alphabetic
                ),
            )
            for number in num_range
        ]

        # Create the html result
        str_show = "<p>"
        for num, string in result:
            str_show += "{}: {}<br>".format(num, string)
        str_show += "</p>"
        flash("FizzBuzz success!")
    except Exception as e:
        flash("Unable to run FizzBuzz. Message: {}".format(e))
        str_show = "Uh oh."

    return render_template("result.html", number=num_show, result=str_show)
