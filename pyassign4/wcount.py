#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Jin-Yu Fu"
__pkuid__  = "1900011813"
__email__  = "Fyun@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """

    wd = ["the", "and", "a", "to", "of", "she", "in", "it", "you", "alice"]
    wdp = [["the     "], ["and     "], ["a       "], ["to      "], \
        ["of      "], ["she     "], ["in      "], ["it      "], \
        ["you     "], ["alice   "]]
    l2 = lines.casefold()
    l2 = l2.replace(".", " ")
    l2 = l2.replace(";", " ")
    l2 = l2.replace(",", " ")
    l2 = l2.replace("!", " ")
    l2 = l2.replace("?", " ")
    l2 = l2.replace("'", " ")
    l2 = l2.replace('"', " ")
    l2 = l2.replace('(', " ")
    l2 = l2.replace(')', " ")
    l2 = l2.replace('[', " ")
    l2 = l2.replace(']', " ")
    l2 = l2.replace(':', " ")
    lst = l2.split()
    for i in range(10):
        wdp[i].append(lst.count(wd[i]))
        wdp[i].reverse()
    wdpr = sorted(wdp)
    wdpr.reverse()
    for i in range(topn):
        print(wdpr[i][1], wdpr[i][0])
    pass
 

if __name__ == "__main__":

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Your key words are too many")

    if len(sys.argv) == 3:
        if sys.argv[2].isdigit():
            if int(float(sys.argv[2])) != float(sys.argv[2]):
                print("Your topn is not a correct integer")
            else:
                if float(sys.argv[2]) < 11 and float(sys.argv[2]) > 0:
                    doc = urlopen(sys.argv[1])
                    text = doc.read()
                    doc.close()
                    text = bytes.decode(text)
                    wcount(text, int(float(sys.argv[2])))
                else: 
                    doc = urlopen(sys.argv[1])
                    text = doc.read()
                    doc.close()
                    text = bytes.decode(text)
                    wcount(text)
        else:
            print("Your topn is not a correct integer")
    
    if len(sys.argv) == 2:
        doc = urlopen(sys.argv[1])
        text = doc.read()
        doc.close()
        text = bytes.decode(text)
        wcount(text)
