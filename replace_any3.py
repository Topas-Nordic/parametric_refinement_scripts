#! /usr/bin/env python

import os
import time
import argparse

def main(xys, inp, out, strID, skip, no_ext):
    """[summary]

    Args:
        xys ([type]): [description]
        inp ([type]): [description]
        out ([type]): [description]
    """

    extensions =[".xy", ".xye", ".raw"]
    if no_ext:
        xys = sorted([f.split('.')[0] for f in os.listdir(xys) if f.endswith(tuple(extensions))])
    else:
        xys = sorted([f for f in os.listdir(xys) if f.endswith(tuple(extensions))])

    z, ze = inp, out

    if strID:
        q = len(strID)

    start = time.time()
    fin, fout = open(z), open(ze, 'a+')  
    s1 = fin.read()
    inp_big = ''
    for i in range(0, len(xys), skip):

        
        inp_replaced = s1.replace(xys[0], xys[i]) # Replacing xdd file
        if strID:
            inp_replaced =  inp_replaced.replace( (strID), f"{i:.{q}d}") # replacing any strIDs e.g. XXXX

        inp_big += '\n' + inp_replaced
        print(xys[i])

        

    fout.write(inp_big)
    fin.close(), fout.close()
    end = time.time()

    print(f"Total time: {end-start} seconds")
           
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

    parser.add_argument('-no_ext', action="store_true", help="Replace filename in big INP including extension.")
    parser.add_argument('-skip', nargs="?", default=1, type=int, help="Integer for taking every nth xy file.")

    args = parser.parse_args()
    args_dict = vars(args)

    main(args_dict['xys'],
         args_dict['inp'],
         args_dict['out'],
         args_dict['id'],
         args_dict['skip'],
         args_dict['no_ext'])
