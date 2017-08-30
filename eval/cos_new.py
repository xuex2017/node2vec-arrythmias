import numpy as np
from scipy import spatial
import operator

#vec key:entityID  value:embedding vector(128d)
vec = {}
'''
vector = np.loadtxt('emb/ArrSample.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/ArrSample.emb', usecols = range(1), skiprows = 1, dtype= int)
'''
vector = np.loadtxt('emb/p1q8.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/p1q8.emb', usecols = range(1), skiprows = 1, dtype= int)

#vector = np.loadtxt('emb/sampleVec.emb', usecols = range(1,5), skiprows = 1)
#entityID = np.loadtxt('emb/sampleVec.emb', usecols = range(1), skiprows = 1, dtype= int)
for index, item in enumerate(vector):
    vec[entityID[index]] = item

cos = []
#cos key: (entity1ID entity2ID) value:cos(entity1, entity2)
for key1, value1 in vec.items():
    for key2, value2 in vec.items():
        if key1 != key2:
            cosine = 1 - spatial.distance.cosine(value1, value2)
            if cosine >=0.7:
                cos.append([int(key1),int(key2),cosine])
        else:
            continue

sorted_cos = sorted(cos, key=lambda x: (x[0], -x[2]))#ann sorted by start up, end down
#sorted_cos = sorted(cos.items(), key = operator.itemgetter(1), reverse = True)
#dic entity_map = {'entityID':'entity'}

entity_map = {}
eType = open('ann/GetEdgeNode/all_entityList.txt')
try:
    lines = eType.readlines()
finally:
    eType.close( )
for line in lines:
    line = line.rstrip('\n')
    ID, entity = line.split(' ',1)
    entity_map[int(ID)] = entity

f = file('eval/p1q8.csv','w')
for index, item in enumerate(sorted_cos):
    print item
    f.write(str(item[0])+'\t'+entity_map[item[0]] + '\t'+\
            str(item[1])+'\t'+entity_map[item[1]] + '\t'+str(item[2])+'\n')
