import numpy as np
from scipy import spatial
import operator

#vec key:entityID  value:embedding vector(128d)
vec = {}
'''
vector = np.loadtxt('emb/ArrSample.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/ArrSample.emb', usecols = range(1), skiprows = 1, dtype= int)
'''
vector = np.loadtxt('emb/directed_p1q16.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/directed_p1q16.emb', usecols = range(1), skiprows = 1, dtype= int)

#vector = np.loadtxt('emb/sampleVec.emb', usecols = range(1,5), skiprows = 1)
#entityID = np.loadtxt('emb/sampleVec.emb', usecols = range(1), skiprows = 1, dtype= int)
for index, item in enumerate(vector):
    vec[entityID[index]] = item


dis = []

dis.append(np.subtract(vec[209],vec[2428]))#BNP
dis.append(np.subtract(vec[212],vec[216]))#EKG
dis.append(np.subtract(vec[277],vec[201]))#AVNRT
dis.append(np.subtract(vec[575],vec[304]))#MRI
dis.append(np.subtract(vec[947],vec[946]))#TEE
dis.append(np.subtract(vec[1289],vec[1287]))#CPR
dis.append(np.subtract(vec[1293],vec[1294]))#GFR
dis.append(np.subtract(vec[1401],vec[358]))#RA
dis.append(np.subtract(vec[1756],vec[1766]))#INR
dis.append(np.subtract(vec[2137],vec[2138]))#PCP
dis.append(np.subtract(vec[2252],vec[1844]))#PT
dis.append(np.subtract(vec[2254],vec[2275]))#APTT
dis.append(np.subtract(vec[2256],vec[2278]))#FDP
dis.append(np.subtract(vec[2297],vec[2274]))#PT_INR
dis.append(np.subtract(vec[2422],vec[2396]))#TOE
dis.append(np.subtract(vec[2427],vec[1482]))#CRP
dis.append(np.subtract(vec[2768],vec[669]))#RBBB
dis.append(np.subtract(vec[3532],vec[3078]))#BUN
dis.append(np.subtract(vec[3585],vec[3586]))#ELISA



for index1, item1 in enumerate(dis):
    for index2,item2 in enumerate (dis):
        cosine = 1 - spatial.distance.cosine(item1, item2)
        print str(index1) + ' ' +str(index2) + ' ' +str(cosine)

#print cosine1
#print cosine1, cosine2, cosine3,cosine4,cosine5
