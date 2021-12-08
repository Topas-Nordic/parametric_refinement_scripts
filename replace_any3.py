#! /usr/bin/env python

import os
import re
import sys
import argparse

def main(xys, inp, out, strID):
    """[summary]

    Args:
        xys ([type]): [description]
        inp ([type]): [description]
        out ([type]): [description]
    """

    ext =[".xy", ".xye", ".raw"]
    xys = sorted([f for f in os.listdir(xys) if f.endswith(tuple(ext))])
    z, ze = inp, out

    if strID:
        q = len(strID)

    for i in range(len(xys)):

        fin, fout = open(z), open(ze, 'a+')  
        s1 = fin.read()

        print(f"next : {xys[i]}")
        fout.write( s1.replace (xys[0], xys[i]))

        if strID:
            fout.write( s1.replace( (strID), f"{i:.{q}d}"))
        fin.close(), fout.close()

           
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Program for making Topas surface refinements.")

    parser.add_argument("xys", type=str, help="Directory of xy files to be refined.")
    parser.add_argument("inp", type=str, help="Path to start .INP file.")
    parser.add_argument("out", type=str, help="Path to store Topas .OUT file")
    parser.add_argument(
        "-id",
        type=str, 
        help="""Unique string identifier for generating unique variables for each refinement file.
             Ex: stringid = XXXX. Allows to refine unique scale factors. scale_XXXX """)

    args = parser.parse_args()
    args_dict = vars(args)

    print(args)

    #main()
