#!/bin/bash

for file in ./*.dcm; do #ciclo su tutti i file.dcm
	newfile=`echo "$file" | cut -d "_" -f 3-5` #rinomino file in newfile passo il risultato a cut che fa come una split e conto da 3 a 5 in base a _	
	#echo "$newfile" 
        mv "$file" $newfile.dcm #rinomino
	
done
