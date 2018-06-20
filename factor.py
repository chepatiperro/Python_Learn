#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import sys, math, argparse, re

###############################################################
# formula: (-b +- sqrt(b^2 - 4*a*c))/2
###############################################################

def factor1(a, b, c):
    return (((-1*b) + math.sqrt(math.pow(b, 2) - (4*a*c)))/(2*a))

def factor2(a, b, c):
    return (((-1*b) - math.sqrt(math.pow(b, 2) - (4*a*c)))/(2*a))


###############################################################
#initiate the parser
###############################################################

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", required=True, help="specify input file")
parser.add_argument("-o", "--outfile", required=True,  help="specify output file")

# read arguments from the command line
args = parser.parse_args()

# Open the files for reading and writing
input_file = open(args.infile)
output_file = open(args.outfile, 'w')

# initialize the regular expression: looking for 3 integers separated by spaces, like this: 10	-23	2
pattern = re.compile(r'^\s*(-?\d+)\s+(-?\d+)\s+(-?\d+)')

line_num = 0

for line in input_file:
    line_num += 1
    (a,b,c) = pattern.search(line).groups()
    x1 = factor1(float(a), float(b), float(c))
    print((x1).as_integer_ratio())
    x2 = factor2(float(a), float(b), float(c))
    print((x2).as_integer_ratio())
    output_file.write("{0:2d}. Input equation: a={1:3d}  b={2:3d}  c={3:3d}\t\tResult: x1={4:5.2f}  x2={5:5.2f}\n".format(line_num, int(a), int(b), int(c), x1, x2))


# Close all open files and quit the program
input_file.close()
output_file.close()
