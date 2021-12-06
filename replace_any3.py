#! /usr/bin/env python

import os
import re
import sys


def main():

    ext =[".xy", ".xye", ".raw"]
    xys = sorted([f for f in os.listdir() if f.endswith(tuple(ext))])
    z, ze = input("input file (including extension): "), input("output file (including extension): ")
    h = input("string to replace: ")
    q = len(h)
    for i in range(len(xys)):

        fin, fout = open(z), open(ze, 'a')  
        s1 = fin.read()

        print(f"next : {xys[i]}")
        fout.write( s1.replace (xys[0], xys[i]))
        #fout.write( s1.replace( (h), f"{i:.qd}")) #sort this out later for replacing a string in start.inp with incrementing numbers
        fin.close(), fout.close()

           
if __name__ == '__main__':
    main()
