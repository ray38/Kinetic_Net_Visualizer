"""
Communicate between Python and Javascript asynchronously using
inter-process messaging with the use of Javascript Bindings.
"""


import csv
import json
import os
import sys




if __name__ == '__main__':
    system_name = sys.argv[1]
    #system_name = "CoFe"

    dirname = system_name + "Graphs"

    block_filename = system_name + "BlockStrucutre.csv"
    hierarchical_filename = system_name + "HierarchicalResultsPerCluster.csv"
    cwd = os.getcwd()

    os.chdir(cwd + "/" + dirname)


    result = {}
    cluster_dict = {}
    with open(block_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                
                time = row[1]
                pulse = row[2]
                cluster = row[3]
                if time not in result.keys():
                    result[time] = {}
                if pulse not in result[time].keys():
                    result[time][pulse] = {}
                result[time][pulse]["cluster"] = row[3]
                result[time][pulse]["nodes"] = []
                result[time][pulse]["links"] = []
                cluster_dict[cluster] = {}
                cluster_dict[cluster]["time"] = time
                cluster_dict[cluster]["pulse"] = pulse
                line_count += 1
                
                
    with open(hierarchical_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                node_list = row[1:]
                line_count += 1
            else:
                cluster = row[0]
                time = cluster_dict[cluster]["time"]
                pulse = cluster_dict[cluster]["pulse"]
                for i, entry in enumerate(row[1:]):
                    temp = {"id":node_list[i],"group":entry}
                    result[time][pulse]["nodes"].append(temp)
                
                cluster_filename = "Optcluster{}.csv".format(cluster)
                with open(cluster_filename) as csv_file2:
                    csv_reader2 = csv.reader(csv_file2, delimiter=',')
                    row2_num = 0
                    for row2 in csv_reader2:
                        #print row2
                        for ii, entry2 in enumerate(row2):
                            if float(entry2) != 0:
                                #print row2_num, ii
                                if node_list[row2_num] != node_list[ii]:
                                    temp = {"source":node_list[row2_num], "target":node_list[ii], "value":abs(float(entry2))}
                                    result[time][pulse]["links"].append(temp)
                        row2_num += 1
                    
                line_count += 1

    for time in result:
        for pulse in result[time]:
            for node in result[time][pulse]["nodes"]:
                temp_node_num_source = 0
                temp_node_num_target = 0
                temp_node_num_both = 0
                
                for link in result[time][pulse]["links"]:
                    if link["source"] == node["id"]:
                        temp_node_num_source +=1
                        temp_node_num_both += 1
                        
                    if link["target"] == node["id"]:
                        temp_node_num_target +=1
                        temp_node_num_both += 1
                
                node["num_source"] = temp_node_num_source
                node["num_target"] = temp_node_num_target
                node["num_both"] = temp_node_num_both
                #print node
    os.chdir(cwd)
    with open('data.json', 'w') as fp:
        json.dump(result, fp, sort_keys=True, indent=4)
