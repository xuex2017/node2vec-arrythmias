import numpy as np
from scipy import spatial
import operator

#vec key:entityID  value:embedding vector(128d)
vec = {}
'''
vector = np.loadtxt('emb/ArrSample.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/ArrSample.emb', usecols = range(1), skiprows = 1, dtype= int)
'''
vector = np.loadtxt('emb/p1q4.emb', usecols = range(1,129), skiprows = 1)
entityID = np.loadtxt('emb/p1q4.emb', usecols = range(1), skiprows = 1, dtype= int)

#vector = np.loadtxt('emb/sampleVec.emb', usecols = range(1,5), skiprows = 1)
#entityID = np.loadtxt('emb/sampleVec.emb', usecols = range(1), skiprows = 1, dtype= int)
for index, item in enumerate(vector):
    vec[entityID[index]] = item

dis = []

dis1 = np.subtract(vec[912],vec[617])#lorazepam-seizure
dis2 = np.subtract(vec[3515],vec[2205])#amlodipine-angina
dis3 = np.subtract(vec[2554],vec[1534])#prednisolone-inflammation
dis4 = np.subtract(vec[3253],vec[506])#isoproterenol-Anesthesia

cosine1 = 1 - spatial.distance.cosine(dis1, dis2)#0.0663345307521
cosine2 = 1 - spatial.distance.cosine(dis3, dis2)#0.307100540114
cosine3 = 1 - spatial.distance.cosine(dis3, dis4)#-0.0827678658901
cosine4 = 1 - spatial.distance.cosine(dis1, dis4)#-0.22556560074
cosine5 = 1 - spatial.distance.cosine(dis2, dis4)#0.190316217404
#print cosine1
print cosine1, cosine2, cosine3,cosine4,cosine5
