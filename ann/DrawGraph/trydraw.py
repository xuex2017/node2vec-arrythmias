import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

G = nx.Graph()
# creat nodeInfo = [ID, Type, entity]

nodeInfo = []

eType = open('DrawGraph/graph_eTypeList.txt')
try:
    lines = eType.readlines()
finally:
    eType.close( )
for line in lines:
    ID, Type, entity = line.split('\t',2)
#    entity = entity.split('\n')
    nodeInfo.append([int(ID), Type, entity])

#add edges from edgelist

edgeInfo = []
edgeNum = open('DrawGraph/graph_edgeList.txt')
try:
    lines = edgeNum.readlines()
finally:
    edgeNum.close( )
for line in lines:
    head_idstr, tail_idstr = line.split(' ')
    head_id = int (head_idstr)
    tail_id = int (tail_idstr)
    edgeInfo.append([nodeInfo[head_id][2], nodeInfo[tail_id][2]])

G.add_edges_from(edgeInfo)

#dic type_map = {'entity':'type'}

type_map = {}
eType = open('DrawGraph/graph_eTypeList.txt')
try:
    lines = eType.readlines()
finally:
    eType.close( )
for line in lines:
    ID, Type, entity = line.split('\t',2)
    type_map[entity] = Type
#dic color_map
color_map = {'Procedure': 'r',
             'Disease_disorder': 'b',
             'Sign_symptom': 'y',
             'Anatomical_structure':'g',
             'Medication':'c' }

values = [color_map.get((type_map.get(node)), 'w') for node in G.nodes()]
#layout = nx.fruchterman_reingold_layout(G)
layout = nx.spring_layout(G)
d = nx.degree(G)
'''
node_color: entity type
node_size: degree
'''
nx.draw(G,pos=layout, node_color=values, with_labels=True,\
        nodelist=d.keys(), node_size=[v * 200 for v in d.values()],\
         alpha = 0.5, font_size = 8, linewidths=0)

plt.savefig("DrawGraph/colorGraph.png")
plt.show()
