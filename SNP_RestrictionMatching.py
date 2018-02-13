#!/usr/bin/env python

##important!! this is for restriction sites that are 6bp long
##Change the coordinate length in row 29 if it's any different
import os, sys, re
from optparse import OptionParser

def main():

    parser = OptionParser(usage="%prog [options]")
    parser.add_option("-r", "--restriction_coordinates", dest="input_file", help="text file containing a list of the restriction site coordinates")
    parser.add_option("-s", "--snp_coordinate", dest="snps", help="text file containing a list of the beginning of snp coordinates")
    parser.add_option("-o", "--output", dest="output_filename", default="SNP_Restriction_matching.txt", help="filename of output")
    parser.add_option
    (options, args) = parser.parse_args()

    with open(options.output_filename, "w") as output_holder:
        output_holder.write("restriction site coords    SNP site coords"+'\n')
        with open(options.snps, "r") as snp, open(options.input_file, "r") as rs:
            snp_coords = []
            restriction_coords = []
            for line in snp:
                snp_coords.append(int(line.strip()))
            for line in rs:
                restriction_coords.append(int(line.strip()))
            for r in restriction_coords:
                for i in snp_coords:
                    if r <= i <= (r + 5):
                        output_holder.write(str(r) + ":" + str(r+5) + "        "+ str(i) + '\n')
    os.rename(options.output_filename, options.output_filename+'_matches')
    sys.exit()

if __name__== '__main__':
    main()
