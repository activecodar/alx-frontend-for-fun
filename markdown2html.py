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
    pass

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        sys.stderr.write("Missing {}\n".format(input_file))
        sys.exit(1)
    sys.exit(0)
