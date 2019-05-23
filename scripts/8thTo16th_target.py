# -*- coding: utf-8 -*-
# Generates a feature file for the 1:16 font weight based on a feature file of the 1:8 weight
# Replaces quavers with crotchets
# NOTE: Used for target glyphs

import re

symbolToLC = {
    'exclam' : 'one',
    'at' : 'two',
    'numbersign' : 'three',
    'dollar' : 'four',
    'percent' : 'five',
    'asciicircum' : 'six',
    'ampersand' : 'seven',
    'asterisk' : 'eight',
    'parenleft' : 'nine',
    'parenright' : 'zero'
}

filename = "test.txt"
outfilename = "test replaced.txt"
with open(outfilename, "wt") as fout:
    with open(filename, "rt") as fin:
        for line in fin:
            if ';' in line and '}' not in line:
                lastWord = [s for s in re.split(r'[\[\];, ]+',line) if s][-2]
                if lastWord.find('.') != -1:
                    pre = lastWord.split('.')[0]
                    if len(pre) == 1:
                        line = line.replace(lastWord, pre.lower() + '.imin')
                    else:
                        line = line.replace(lastWord, symbolToLC[pre] + '.imin')
                else:
                    if len(lastWord) == 1:
                        line = line.replace(lastWord, lastWord.lower() + '.min')
                    elif lastWord in symbolToLC:
                        line = line.replace(lastWord, symbolToLC[lastWord] + '.min')
            fout.write(line)
