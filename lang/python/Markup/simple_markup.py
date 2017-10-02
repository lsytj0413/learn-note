# coding=utf-8

import sys, re
from util import *


print '<html><head><title>...</title></head><body>'

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+)\*', r'<em>\1</em>', block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'


"""
usage:
python simple_markup.py < test_input.txt > test_output.html
"""
