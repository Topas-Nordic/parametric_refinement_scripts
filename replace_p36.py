#! /usr/bin/env python
x,y = int(input("first file number: ")), int(input("last file number : "))
z, ze = input("input file (including extension): "), input("output file (including extension): ")
q = x-1
while q<y:
    q = q+1
    fin, fout = open(z), open(ze, 'a')
    out = '{0}'.format(q)
    s1 = fin.read()
    fout.write( s1.replace ('001', out))
    fin.close(), fout.close()
    continue
       



