#!/usr/bin/env python3

import os
import os.path
import re
import argparse


def get_parameters():
    """Get parameters from user input."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", dest="input_file", action="store")
    parser.add_argument("--output-file", dest="output_file", action="store")
    parser.add_argument("--original", dest="original_word", action="store")
    parser.add_argument("--replacement", dest="replacement_word", action="store")
    args = parser.parse_args()

    return args


def find_and_replace(input_file, output_file, original_word, replacement_word):

    # Variable for storing converted data.
    converted_data = []

    # Read file.
    with open(input_file) as f:
        data = f.readlines()

    # Find and replace content.
    for row in data:
        row = re.sub(original_word, replacement_word, row.rstrip())
        converted_data.append(row)

    # Write to file.
    with open(output_file, "w") as f:
        for row in converted_data:
            f.write(row + "\n")


def validate_input_file(i):

    valid = True

    while True:

        # Validate input file path exists.
        if os.path.exists(i) is False:
            print("Error. Couldn't find input file: " + i)
            valid = False
            break

        # Validate input file is a file.
        if os.path.isfile(i) is False:
            print("Error. Input file is not a file.")
            valid = False
            break

        # Validate file size. Maximum is 10mb.
        if os.path.getsize(i) > 600:
            print("Error. Input file is too large (max 10mb).")
            valid = False
            break

        valid = True

        break

    return valid


def main():

    input_file = get_parameters().input_file
    output_file = get_parameters().output_file
    original_word = get_parameters().original_word
    replacement_word = get_parameters().replacement_word

    valid = validate_input_file(input_file)

    if valid == True:
        find_and_replace(input_file, output_file, original_word, replacement_word)


if __name__ == "__main__":
    main()
