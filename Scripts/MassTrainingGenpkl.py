import csv
import collections
import pickle
path ="/media/federica/Loserino/CBIS-DDSM/manifest-Egq0PU078220738724328010106/Mass-Training/"
ifile  = open(path+"metadata.csv", "r")
read = csv.reader(ifile)
numeri = []
for row in read :
    if row[4] == "Subject ID":
        continue
    #print (row[4])


    l = row[4].split("_")
    #valore_fisso = l[1];
    numero = l[2];
    numeri.append(numero)
numeri.sort()



res = [item for item, count in collections.Counter(numeri).items() if count == 4] #list comprehension genera lista a partire da un'altra lista
#print(len(res))
esami = []
#[{'horizontal_flip': 'NO', 'L-CC': ['0_L_CC'], 'L-MLO': ['0_L_MLO'], 'R-MLO': ['0_R_MLO'], 'R-CC': ['0_R_CC']}
for n in res:
    esame = {'horizontal_flip': 'NO',
                  'L-CC': [n+"_LEFT_CC"],
                  'L-MLO': [n+'_LEFT_MLO'],
                  'R-MLO': [n+'_RIGHT_MLO'],
                  'R-CC': [n+'_RIGHT_CC']
                  }
    #print(dizionario)
    esami.append(esame)
print(esami)


file_name = path + 'exam_list_before_cropping.pkl'
with open(file_name, 'wb') as handle:
    pickle.dump(esami, handle) #crea file binario con dentro scritto esami





