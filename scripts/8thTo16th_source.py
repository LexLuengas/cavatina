# -*- coding: utf-8 -*-
# Generates a feature file for the 1:16 font weight based on a feature file of the 1:8 weight
# Replaces quavers with crotchets
# NOTE: Used for source glyphs

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

def replacePrefix(string):
    frag = string.split('.')
    if len(frag[0]) == 1:
        if '.' in string:
            frag[0] = frag[0].lower() + '.imin'
        else:
            frag[0] = frag[0].lower() + '.min'
    else:
        if '.' in string:
            frag[0] = symbolToLC[frag[0]] + '.imin'
        else:
            frag[0] = symbolToLC[frag[0]] + '.min'
    return frag[0]


filename = "test.txt"
outfilename = "test replaced.txt"
with open(outfilename, "wt") as fout:
    with open(filename, "rt") as fin:
        for line in fin:
            if ';' in line and '}' not in line:
                splitLine = line.split()
                begin = False
                for i in range(len(splitLine)):
                    if '[' in splitLine[i] and '@' not in splitLine[i]:
                        begin = True
                    if begin:
                        if '[' in splitLine[i]:
                            splitLine[i] = '[' + replacePrefix(splitLine[i][1:])
                        elif ']' in splitLine[i]:
                            splitLine[i] = replacePrefix(splitLine[i][:-2]) + "]'"
                        else:
                            splitLine[i] = replacePrefix(splitLine[i])
                    if begin and ']' in splitLine[i]:
                        break
                    if not begin and splitLine[i][0].isupper():
                        splitLine[i] = replacePrefix(splitLine[i][:-1]) + "'"
                line = '  ' + ' '.join(splitLine) + '\r\n'
            fout.write(line)
