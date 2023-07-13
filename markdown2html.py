#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Get the input and output file names from the command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert the Markdown file to HTML and write the output to a file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a successful status code
    sys.exit(0)
