# -*- coding: utf-8 -*-
"""Generates feature files for multiple keyboard layouts based on the feature file for the english (US) keyboard layout.

Usage:
    # Generate all target keyboard layouts
    python2 remap_feature.py features_US.fea 

    # Generate a specific target keyboard layout
    python2 remap_feature.py features_US.fea DE
"""

import sys
import re
from keyboard_layouts import getGlyphNamesofLayout

languageList = ['DE', 'SPi', 'FR', 'IT', 'PTb', 'PTp', 'PTa',
                'SP', 'BRw', 'BRa'] if len(sys.argv) < 3 else [sys.argv[2]]
usGlyphNames = getGlyphNamesofLayout('US')

if len(sys.argv) < 2:
    print "No feature file name given."
    sys.exit()

filename = sys.argv[1]

for lang in languageList:
    print 'Processing %s...' % lang
    outGlyphNames = getGlyphNamesofLayout(lang)
    zipped = zip(usGlyphNames, outGlyphNames)  # (FROM , TO)
    outfilename = "feature %s.fea" % lang

    with open(outfilename, "wt") as fout:
        with open(filename, "rt") as fin:
            for line in fin:
                for i, (subfrom, subto) in enumerate(zipped):
                    tempName = 'temp%03d' % (i,)
                    p = re.compile(r'\b{glyph}\b(?!\.)'.format(glyph=subfrom))
                    line = p.sub(tempName, line)
                for i, (subfrom, subto) in enumerate(zipped):
                    tempName = 'temp%03d' % (i,)
                    p = re.compile(r'\b{glyph}\b(?!\.)'.format(glyph=tempName))
                    line = p.sub(subto, line)
                fout.write(line)
