#!/usr/bin/env python2
'''
Read all .txt files within the current directory, and produce a spreadsheet
with one column for filename and another for the highest apparent parenthetical
money figure.

This is a hack and has loads of problems, but it worked at the Hackathon.
'''
import os
import re

def main():
    print "filename,money"
    for file in os.listdir("."):
        if file[-4:] != ".txt":
            continue
        print file + "," + read_text(file)

def read_text(file):
    text = open(file).read()
    text_sans_space = text.replace("\n", " ").replace(" ", "")
    money_raw = re.findall(r"\(\$[.,0-9]+\)", text_sans_space)
    if len(money_raw) > 0:
        money = [filter(lambda c: c in ",1234567890", m).replace(",", ".") for m in money_raw]
        big = sorted(money)[0]
        return big
    else:
        return ""

#read_text("P-137-11.txt")
main()
