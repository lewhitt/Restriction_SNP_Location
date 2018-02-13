#!/usr/bin/env python

import os, sys, re
from optparse import OptionParser

def main():
    parser=OptionParser(usage="%prog[options]")
    parser.add_option("-r", "--restrSeq", dest="restrictionSeq", help="restriction sequence")
    parser.add_option("-o", "--output", dest="output_file", default="CdRestrictionSiteLocator_output.txt", help="name of output file with the coordinates of all site matches")
    (options, args) = parser.parse_args()
    with open("Zea_mays.AGPv3.22.dna.chromosome.2.cd.mapping.section.fa", "r") as file:
        for line in file.readlines():
            if line[0] == ">":
                pass
            else:
                chr2_region = line.strip()
                ##print chr2_region[780:786]
                ##print chr2_region[168990545-159243918:168990551-159243918] 
                pattern = str(options.restrictionSeq)
                regex = re.compile(pattern)
                with open("outputHolder", "w") as output:
                    for match in regex.finditer(chr2_region):
                        correct = match.start()+ 159243918
                        output.write(str(correct)+'\n')
    os.rename("outputHolder", options.output_file+'_sites')
    sys.exit()
if __name__ == '__main__':
    main()
