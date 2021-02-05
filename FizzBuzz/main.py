#! /usr/bin/env python3

import os

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from .lib.objects import FizzBuzz
from .lib.funcs import run_fizz_buzz


main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")


@main.route("/execute", methods=["POST"])
def execute():
	request_dict = request.form.to_dict()
	print (request_dict)
	fb_data = [(k, int(v.strip("/"))) for k, v in request_dict.items() if "fb" not in k]
	fb_list = [FizzBuzz(*fb) for fb in fb_data]

	number = int(request_dict.get("fbNumber"))
	separator = str(request_dict.get("fbSeparator"))

	sort_numeric = False
	sort_alphabetic = False

	if "fbSortNumeric" in request_dict:
		if request_dict["fbSortNumeric"] == "on":
			sort_numeric = True
	elif ("fbSortAlphabetical" in request_dict):
		if request_dict["fbSortAlphabetical"] == "on":
			sort_alphabetic = True

	result = run_fizz_buzz(number, fb_list, separator, sort_numeric, sort_alphabetic)

	return render_template("result.html", number=number, result=result)