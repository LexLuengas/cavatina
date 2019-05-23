# -*- coding: utf-8 -*-
# Re-partitions the feature lookup blocks to conform to a specific max. block size

filename = "feature US.txt"
outfilename = "frag feature US.txt"

with open(outfilename, "wt") as fout:
    with open(filename, "rt") as fin:
        lookupsize = 50
        lookupcount = 0
        count = 0
        wascontextual = False
        calt = False
        for line in fin:
            if calt:
                if count == 0:
                    startenclose = '  lookup lu%03d useExtension{\n' % (lookupcount,)
                    fout.write(startenclose)
                    count += 1
                if ('{' not in line) and ('}' not in line) and (';' in line):
                    if not(wascontextual == ("'" in line)): # group contextual substitutions and ligature in respective lookup blocks
                        wascontextual = not wascontextual
                        endenclose = '  } lu%03d;\n\n' % (lookupcount,)
                        fout.write(endenclose)
                        lookupcount += 1
                        startenclose = '  lookup lu%03d useExtension{\n' % (lookupcount,)
                        fout.write(startenclose)
                        count = 0
                    fout.write(line)
                    count += 1
                if count == lookupsize:
                    endenclose = '  } lu%03d;\n\n' % (lookupcount,)
                    fout.write(endenclose)
                    lookupcount += 1
                    count = 0
            else:
                fout.write(line)
                if 'liga;' in line:
                    calt = True
                    fout.write('feature calt {\n')
        if count != lookupsize:
            endenclose = '  } lu%03d;\n\n' % (lookupcount,)
            fout.write(endenclose)
        fout.write('} calt;\n')
                