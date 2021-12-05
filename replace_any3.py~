#! /usr/bin/env python

import os
import re
import sys


def main():

    xys = sorted([f for f in os.listdir() if f.endswith(".xy")])
    z, ze = input("input file (including extension): "), input("output file (including extension): ")

    for i in range(len(xys)):

        fin, fout = open(z), open(ze, 'a')  
        s1 = fin.read()

        print(f"next : {xys[i]}")
        fout.write( s1.replace (xys[0], xys[i]))
        fin.close(), fout.close()

           
if __name__ == '__main__':
    main()