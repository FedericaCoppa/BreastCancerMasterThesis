import csv
import collections
import pickle
import os
import shutil
path ="/home/federica/Desktop/TesiMagistrale/sample_output_mass_test/"
ifile  = open(path+"mass_description_test.csv", "r")
read = csv.reader(ifile)



for row in read :
	if row[9] == "pathology":
		continue
	if row[9] == "BENIGN":
		newpath = r'/home/federica/Desktop/TesiMagistrale/sample_output_mass_test/benign' 
		if not os.path.exists(newpath):
			os.makedirs(newpath)
	if row[9] == "MALIGNANT":
		newpath = r'/home/federica/Desktop/TesiMagistrale/sample_output_mass_test/malign' 
		if not os.path.exists(newpath):
			os.makedirs(newpath)
	if row[9] == "BENIGN_WITHOUT_CALLBACK":
		newpath = r'/home/federica/Desktop/TesiMagistrale/sample_output_mass_test/benign_without_callback' 
		if not os.path.exists(newpath):
			os.makedirs(newpath)
	original = "/home/federica/Desktop/TesiMagistrale/sample_output_mass_test/cropped_images/" +row[0][2:] + "_" + row[2] + "_" + row[3] + ".png"
	target = newpath
	try:
		shutil.move(original,target)
	except:
		print('esiste già!')
	
