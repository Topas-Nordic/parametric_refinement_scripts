# This is a program to convert diffraction data in ".qy" (from pyFAI)
# or ".chi" (from fit2D) format to ".xy",".xye" or and ".gsa" format
# used by your preferred refinement software.
#
# If you have questions please contact: jonas.sottmann@smn.uio.no
#
import sys
import os
import math
import shutil
import time

def yes_or_no():
	q1 = raw_input('>')
	if q1 == '' or q1 == 'Y' or q1 == 'y':
		return True
	if q1 == 'N' or q1 == 'n':
		return False
	while q1 != '' or q1 != 'Y' or q1 != 'y' or q1 != 'N' or q1 != 'n':
		print "I did not understand you. Please answer again! (Y)/N?"
		q1 = raw_input('>')
		if q1 == '' or q1 == 'Y' or q1 == 'y':
			return True
		if q1 == 'N' or q1 == 'n':
			return False

	

list = []	
				
print "This is a program to convert diffraction data in \".qy\" (from pyFAI)"
print "or \".chi\" (from fit2D) format to \".xy\",\".xye\" or and \".gsa\" format"
print "used by your preferred refinement software."
print "\n"
print "If you have questions please contact: jonas.sottmann@smn.uio.no"
print "\n"
print "The possible files to convert are:"
for file_name in (os.listdir(os.curdir)):
	if file_name.endswith('.qy') or file_name.endswith('.chi'):
		print file_name
print ""
print "Would you like to convert all files of this folder? (Y)/N?" 
if yes_or_no():
	print "All files will be converted"
	for file_name in (os.listdir(os.curdir)):
		if file_name.endswith('.qy') or file_name.endswith('.chi'):
			list.append(file_name)
else:
	print "Please confirm which files you want to convert:"
	for file_name in (os.listdir(os.curdir)):
		if file_name.endswith('.qy') or file_name.endswith('.chi'):
				print file_name, "(Y)/N?"
				if yes_or_no():
					list.append(file_name)
							
print "Is the wavelength 0.1777900 AA? (Y)/N?"
if yes_or_no():
	LAMBDA = 0.1777900
	pass
else:
	condition = 1
	while condition:
		try: 
			LAMBDA =float(raw_input("lambda:"))
			print "Is the wavelength 0.1777900 AA? (Y)/N?" % (LAMBDA)
			if yes_or_no():
				condition = 0
		except(ValueError):
			print "Please enter a valid wavelength!"
							
print "Do you want to convert to \".xy\"? (Y)/N?" 
q_xy= yes_or_no()

print "Do you want to convert to \".xye\"? (Y)/N?" 
q_xye = yes_or_no()

print "Do you want to convert to \".gsa\"? (Y)/N?" 
q_gsa = yes_or_no()

print "Do you want to use an angular range of 0 to 200 deg in 2theta? (Y)/N?"
if yes_or_no():
	start= 0.0
	end=200.0
	pass
else:
	condition = 1
	while condition:
		try: 
			start=float(raw_input("Start:"))
			end= float(raw_input("End  :"))
			print "Do you want to use an angular range of %f to %f deg in 2theta? (Y)/N?" % (start,end)
			if yes_or_no():
				condition = 0
		except(ValueError):
			print "Please enter a valid angle!"

for file_name in list:
	if file_name.endswith('.qy') or file_name.endswith('.chi'):
		x_min = 1000.0
		x_max = 0.0
		nb_lines = 0
		f = open(file_name, 'r')
		if q_xy:
			g = open(file_name.replace('.qy','.xy').replace('.chi','.xy'), 'w')
		if q_xye or q_gsa:
			a = open(file_name.replace('.qy','.xyedummy').replace('.chi','.xyedummy'), 'w')
		for line in f:
			l = line.rstrip(os.linesep)
			l = l.replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ').replace('  ',' ')
			if l != '':
				data = l.split('\t')
				try:
					angle = 2.0 * 180.0 / math.pi * math.asin( float(data[0]) * LAMBDA / 4.0 / math.pi)
					if angle >= start and angle <= end:
						I = float(data[1])
						# if file_name.endswith('.qy'):
							# stdv = float(data[2])
						if file_name.endswith('.qy'):
							if I >= 0.0:
								stdv = math.sqrt(I)
							else:
								stdv = 0.1
						if q_xy:
							g.write("%2.10f %.10f\n" % (angle, I))
						if q_xye or q_gsa:
							a.write("%2.10f %.10f %.10f\n" % (angle, I, stdv))
						if angle < x_min:
							x_min = angle
						if angle > x_max:
							x_max = angle
						nb_lines += 1
				except(IndexError):
					pass
				except(ValueError):
					pass
		step = round(((x_max-x_min)/float(nb_lines-1)),6)
		# step = ((x_max-x_min)/float(nb_lines-1))
		# print step
		f.close()
		if q_xy:
			g.close()
			print file_name + " converted to " + file_name.replace('.qy','.xy').replace('.chi','.xy') 
		if q_xye or q_gsa:
			a.close()
		
	
	if 	q_gsa:	
		g = open(file_name.replace('.qy','.xyedummy').replace('.chi','.xyedummy'), 'r')
		h = open(file_name.replace('.qy','.gsa').replace('.chi','.gsa'), 'w')
		# Sat Feb 22 09:43:22 2014  /buffer/ld0132/Powder/USERS_2014/Serena/FMNHC021DA_50
		# Instrument parameter      id31.prm                                              
		# BANK 1   10833    2167 CONST   300.000     0.300  0.0 0.0 ESD  
		# BANK 1 3985 797 CONST 117.0625 0.97 0 0 ESD        
		# ('BANK',3I,A,4F,A)IBANK,NCHAN,NREC,BINTYP,(BCOEF(I),I=1,4),TYPE
		#
		# write title
		hline =  file_name.replace('.qy','').replace('.chi','')
		while len(hline) < 80:
			hline += ' '
		hline += '\n'
		h.write(hline)
		hline = ''
		#
		# write header
		BANK = 'BANK'
		IBANK = '1'
		NCHAN = ('%d' % nb_lines)
		entries_per_line = 5
		nrec = math.ceil(nb_lines/entries_per_line)
		NREC = ('%d' % nrec)
		BINTYP = 'CONST'
		BCOEF = ('%f %.3f 0 0' % (x_min*100, step*100))
		TYPE = 'ESD'
		hline= 'BANK' +' '+ IBANK +' '+ NCHAN +' '+ NREC +' '+ BINTYP +' '+ BCOEF +' '+ TYPE
		while len(hline) < 80:
			hline += ' '
		hline += '\n'
		h.write(hline)
		hline = ''
		#
		# write data lines
		i=0
		for line in g:
			l = line.rstrip(os.linesep)
			data = l.split(' ')
			I = float(data[1])
			#if I >= 0.0:
			#	sigma = math.sqrt(I)
			#else:
			#	sigma = 0.1
			sigma = float(data[2])
			I = str(I)
			I = I[0:7]
			while len(I) < 7:
				I += ' '
			sigma = str(sigma)
			sigma = sigma[0:7]
			while len(sigma) < 7:
				sigma += ' '
			hline += ('%s %s ' % (I,sigma))
			i+=1
			if i==entries_per_line:
				hline += '\n'
				h.write(hline)
				hline = ''
				i=0
		if i!=0:
			hline += (entries_per_line-i)*'        '
			hline += '\n'
			h.write(hline)
			hline = ''
		h.close()
		g.close()
		print file_name + " converted to " + file_name.replace('.qy','.gsa').replace('.chi','.gsa')
	#renaming or removal of the dummy file 
	if q_xye:
		try:
			os.remove(file_name.replace('.qy','.xye').replace('.chi','.xye'))
		except(WindowsError):
			pass
		shutil.move(file_name.replace('.qy','.xyedummy').replace('.chi','.xyedummy'), file_name.replace('.qy','.xye').replace('.chi','.xye'))
		print file_name + " converted to " + file_name.replace('.qy','.xye').replace('.chi','.xye') 
	if q_gsa and q_xye != True:
		os.remove(file_name.replace('.qy','.xyedummy').replace('.chi','.xyedummy')) 
		
print "done"
time.sleep(15)
