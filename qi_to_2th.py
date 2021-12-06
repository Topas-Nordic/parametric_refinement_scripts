#! /usr/bin/env python

import os
import numpy as np
import pandas as pd
import re
import math


ext =[".qI"]
qis = sorted([f for f in os.listdir() if f.endswith(tuple(ext))])
lam = 0.2138

for i in qis:
    df2=pd.read_csv(i, header=None, delim_whitespace=True)
    df2[0] = df2[0].apply(lambda x: 2*(180/math.pi)*math.asin((x*lam)/(4*math.pi)))
    df2[1] = df2[1].apply(lambda x: 10*x)
    filename = i[:-3]
    df2.to_csv(f"{filename}.xy", sep='\t', header=False, index=False)