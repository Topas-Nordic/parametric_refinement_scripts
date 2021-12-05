#! /usr/bin/env python
x,y = int(input("first file number: ")), int(input("last file number : "))
h = input("string to replace: ")
z, ze = input("input file (including extension): "), input("output file (including extension): ")
q = x-1
while q<y:
    q = q+1
    fin, fout = open(z), open(ze, 'a')
    out = '{0}'.format(q)
    s1 = fin.read()
    fout.write( s1.replace ((h), out))
    fin.close(), fout.close()
    continue
       



