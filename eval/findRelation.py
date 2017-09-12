import numpy as np
from scipy import spatial
import operator

#vec key:entityID  value:embedding vector(128d)
vec = {}
'''
vector = np.loadtxt('emb/ArrSample.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/ArrSample.emb', usecols = range(1), skiprows = 1, dtype= int)
'''
vector = np.loadtxt('emb/p1q16.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/p1q16.emb', usecols = range(1), skiprows = 1, dtype= int)

#vector = np.loadtxt('emb/sampleVec.emb', usecols = range(1,5), skiprows = 1)
#entityID = np.loadtxt('emb/sampleVec.emb', usecols = range(1), skiprows = 1, dtype= int)
for index, item in enumerate(vector):
    vec[entityID[index]] = item


dis = []

dis.append(np.subtract(vec[912],vec[617]))#lorazepam-seizure
dis.append(np.subtract(vec[912],vec[625]))#lorazepam-seizure
dis.append(np.subtract(vec[912],vec[3334]))#lorazepam-seizure
dis.append(np.subtract(vec[939],vec[1534]))#prednisone-inflammation
dis.append(np.subtract(vec[1172],vec[1097]))#mitoxantrone-MS
dis.append(np.subtract(vec[1602],vec[54]))#ceftriaxone-infections
dis.append(np.subtract(vec[1602],vec[55]))#ceftriaxone-infections
dis.append(np.subtract(vec[2554],vec[1534]))#prednisolone-inflammation
dis.append(np.subtract(vec[2554],vec[1097]))#prednisolone-ms
dis.append(np.subtract(vec[2554],vec[2612]))#prednisolone-arthritis
dis.append(np.subtract(vec[3253],vec[506]))#isoproterenol-Anesthesia
dis.append(np.subtract(vec[3253],vec[1038]))#isoproterenol-Anesthesia
dis.append(np.subtract(vec[3253],vec[1037]))#isoproterenol-Anesthesia
dis.append(np.subtract(vec[3515],vec[2205]))#amlodipine-angina
dis.append(np.subtract(vec[3824],vec[1534]))#methylprednisolone-inflammation
dis.append(np.subtract(vec[3824],vec[1195]))#methylprednisolone-allergies



for index1, item1 in enumerate(dis):
    for index2,item2 in enumerate (dis):
        cosine = 1 - spatial.distance.cosine(item1, item2)
        print str(index1) + ' ' +str(index2) + ' ' +str(cosine)

#print cosine1
#print cosine1, cosine2, cosine3,cosine4,cosine5
