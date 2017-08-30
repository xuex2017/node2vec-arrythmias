'''
input: .ann file (example.txt)
output: new_entityList.txt, new_edgelist.txt, eType_list
        ann = [['Type','start','end','entity']]
        edge created by line order of case report, to be modified
'''
import numpy as np
import os
import getfilename
import networkx as nx
import matplotlib.pyplot as plt


def get_nodelist(entity_list, File_name, ann, eType_list): #create entityList file, new add eType_list

    all_the_text = open(File_name)
    try:
        lines = all_the_text.readlines()
    finally:
        all_the_text.close( )

    for line in lines:
        ID, Type_start_end, entity = line.split('\t',2)
        Type, start_str, end_str = Type_start_end.split(' ',2)
        start = int(start_str)
        end = int(end_str)
        ann.append([Type, start, end, entity])

        if entity not in entity_list:
            entity_list.append(entity)
            eType_list.append([Type, entity])
    f = file('DrawGraph/graph_entityList.txt', 'w') # open for 'w'riting
    f1 = file('DrawGraph/graph_eTypeList.txt', 'w') #new
    for index, item in enumerate(entity_list):
        f.write(str(index) + ' ' + item) # write text to file
        f1.write(str(index) + '\t' + eType_list[index][0] +'\t'+ item)#new
    return entity_list


def get_edgelist(edge_list,File_name,ann,entity_list):#get edge list for one case report ann

#edge_list: existing edgeList
#File_name: current case report
#ann: current case report ann
#entity_list: full entity list

#    entity_list = get_nodelist(File_name,ann)
    sorted_ann = sorted(ann, key=lambda x: (x[1], -x[2]))#ann sorted by start up, end down
    main_entity = []
    modifier_entity = []
    main_edge = []
    modifier_edge = []

    for index,item in enumerate(sorted_ann):
        cur_index = entity_list.index(item[3])#find index of current index
        cur_start = item[1]
        cur_end = item[2]
        if index == 0:
            main_entity.append(item)
        elif index > 0 and cur_start > main_entity[-1][2]:
            main_entity.append(item)
        else:
            if entity_list.index(item[3]) != entity_list.index(main_entity[-1][3]):
                modifier_entity.append(item)
                modifier_edge.append([entity_list.index(item[3]),entity_list.index(main_entity[-1][3])])

    for index,item in enumerate(main_entity):
        cur_index = entity_list.index(item[3])#find index of current index
        if index > 0:
            last_index = entity_list.index(main_entity[index-1][3])
            main_edge.append( [last_index, cur_index])

    print File_name
    print 'main edge:'
    print main_edge
    print 'modifier edge:'
    print modifier_edge
    print '\n'

    f = file('DrawGraph/graph_edgeList.txt', 'w') # open for 'w'riting
    main_edge.extend(modifier_edge)
    for edge in main_edge:
        if edge not in edge_list:
            edge_list.append(edge)

    for index, item in enumerate(edge_list):
        f.write(str(item[0]) + ' ' + str(item[1]) + '\n' ) # write text to file
    return edge_list

def main():
    ann = []
    entity_list = []
    eType_list = []#entity type list
    edge_list = []
    label_el=[]#label of edge list node
    fname =  getfilename.GetFileList('Arrhythmias/sample','ann')
    for fn in fname:
        ann=[]
        entity_list = get_nodelist(entity_list, fn, ann, eType_list)#new add eType_list
        edge_list = get_edgelist(edge_list,fn, ann, entity_list)

    for index, edge in enumerate(edge_list):
        label_el.append([entity_list[edge[0]],entity_list[edge[1]]])
'''
    G = nx.Graph()
    G.add_edges_from(label_el)
    colors = []
#    for index, label in enumerate(label_el):
    eType = open('DrawGraph/graph_eTypeList.txt')
    try:
        lines = eType.readlines()
    finally:
        eType.close( )

    for line in lines:
        ID, Type, entity = line.split('\t',2)
        for index, label in enumerate(label_el):
            if label == entity:
                colors.append(Type)
    for index, item in enumerate(colors):
        print 'color'+ colors[index]

    layout = nx.random_layout(G)
    nx.draw(G,pos=layout, with_labels = True, node_size = 300, alpha = 0.5, font_size = 8, node_color = ['r','b','y'])
    plt.savefig("DrawGraph/sample_graph.png")

#    plt.show()

'''

if __name__ == "__main__":
	main()
