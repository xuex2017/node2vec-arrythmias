import numpy as np
from scipy import spatial
import operator

#vec key:entityID  value:embedding vector(128d)
vec = {}
'''
vector = np.loadtxt('emb/ArrSample.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/ArrSample.emb', usecols = range(1), skiprows = 1, dtype= int)
'''
vector = np.loadtxt('emb/Arrhythmias.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/Arrhythmias.emb', usecols = range(1), skiprows = 1, dtype= int)

#vector = np.loadtxt('emb/sampleVec.emb', usecols = range(1,5), skiprows = 1)
#entityID = np.loadtxt('emb/sampleVec.emb', usecols = range(1), skiprows = 1, dtype= int)
for index, item in enumerate(vector):
    vec[entityID[index]] = item

cos = {}
#cos key: (entity1ID entity2ID) value:cos(entity1, entity2)
for key1, value1 in vec.items():
    for key2, value2 in vec.items():
        if key1 != key2:
            cosine = 1 - spatial.distance.cosine(value1, value2)
            if cosine >=0.8:
                cos[(key1, key2)] = cosine
        else:
            continue

sorted_cos = sorted(cos.items(), key = operator.itemgetter(1), reverse = True)

f = file('eval/sorted_cosine_similarity.txt','w')
for index, item in enumerate(sorted_cos):
    print item
    f.write(str(item)+'\n')
