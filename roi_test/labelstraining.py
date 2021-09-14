import csv
import collections
import pickle
import os
import shutil
path ="/home/federica/Desktop/TesiMagistrale/scripts/roi_test/"
ifile  = open(path+"calc_case_description_test_set.csv", "r")
read = csv.reader(ifile)



for row in read :
	if row[9] == "pathology":
		continue
	if row[9] == "BENIGN":
		newpath = r'/home/federica/Desktop/TesiMagistrale/nuovo_calc_test/benign' 
		if not os.path.exists(newpath):
			os.makedirs(newpath)
	if row[9] == "MALIGNANT":
		newpath = r'/home/federica/Desktop/TesiMagistrale/nuovo_calc_test/malign' 
		if not os.path.exists(newpath):
			os.makedirs(newpath)
	if row[9] == "BENIGN_WITHOUT_CALLBACK":
		newpath = r'/home/federica/Desktop/TesiMagistrale/nuovo_calc_test/benign_without_callback' 
		if not os.path.exists(newpath):
			os.makedirs(newpath)
	original = "/home/federica/Desktop/TesiMagistrale/scripts/roi_test/" +row[0][2:] + "_" + row[2] + "_" + row[3] + ".png"
	target = newpath
	try:
		shutil.move(original,target)
	except:
		print('esiste già!')
	
