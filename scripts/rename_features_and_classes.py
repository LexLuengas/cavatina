# -*- coding: utf-8 -*-
"""Renames classes and features to shorter names"""
import re

filename = "classes US.txt"
outfilename = "classes US (min).txt"
classMap = {}

i = 0 # enumerate classes
with open(outfilename, "wt") as fout:
    with open(filename, "rt") as fin:
        for line in fin:
            if line.find(r"%%CLASS") > -1:
                oldClassName = line.split()[1]
                newClassName = "c%X" % i
                classMap[oldClassName] = newClassName
                i += 1
                line = r"%%CLASS " + newClassName + "\n"
            fout.write(line)

filename = "feature US.fea"
outfilename = "feature US (min).fea"

with open(outfilename, "wt") as fout:
    with open(filename, "rt") as fin:
        for line in fin:
            l = []
            for w in line.split():
                if w[0] == "#":
                    break
                if "@" in w:
                    for subfrom, subto in classMap.items():
                        p = re.compile(r'([ \[\]\']?@){s}((?!\.)[ \[\]\';]?\b)'.format(s = subfrom))
                        newW, subNo = p.subn(r"\1" + subto + r"\2", w)
                        if subNo:
                            w = newW
                            break
                l.append(w)
            l.append("\n")
            line = " ".join(l)
            if len(line) > 4:
                fout.write(line)

