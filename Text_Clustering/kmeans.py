import sys
import random
import math
def main():
    cluster_num = 2#int(sys.argv[1])
    file_name = "DATA.txt"#sys.argv[2]
    vector_list = list()
    # METHOD#1: get vector by tf
    f = open(file_name)
    f_line = f.readline()
    while '' != f_line:
        v=get_list_tf(f_line)
        print v
        vector_list.append(v)
        f_line = f.readline()
    f.close()
    # METHOD#1: generate centroid indexes randomly
    centroid_index_list = random.sample(list(range(0, len(vector_list)-1)), cluster_num)    
    centroid_list = list()
    for centroid_index in centroid_index_list:
        centroid_list.append(vector_list[centroid_index])

    # GENERATE CLUSTERS
    clusters = dict()  
    stop = False
    itr = 0
    while not stop:
        itr += 1
        # cluster each vector
        clusters.clear()
        for v_index, vector in enumerate(vector_list):
            max_sim = sys.float_info.min
            classification_res = 0
            for c_index, centroid in enumerate(centroid_list):
                cur_dis = get_dis(vector, centroid)
                if cur_dis > max_sim:
                    max_sim = cur_dis
                    classification_res = c_index

            if classification_res in clusters:
                # update
                clusters[classification_res].append(v_index)
            else:
                # add
                clusters[classification_res] = list()
                clusters[classification_res].append(v_index)

        # RECALCULATE CLUSTERS' CENTERS
        old_centroid_list = list(centroid_list)
        for key, cluster in clusters.iteritems():   
            # update the center for current cluster
            v1 = vector_list[cluster[0]]
            index = 1
            while index < len(cluster):
                v2 = vector_list[cluster[index]]

                i1 = 0
                i2 = 0

                while i1 < len(v1) and i2 < len(v2):
                    if v1[i1][0] == v2[i2][0]:
                        v1[i1] = (v1[i1][0], (v1[i1][1] + v2[i2][1]))
                        i1 += 1
                        i2 += 1
                    elif v1[i1][0] > v2[i2][0]:     # add [i2] in front of i1 & move i2 ++
                        v1.insert(i1, (v2[i2][0], v2[i2][1]))
                        i1 += 1
                        i2 += 1
                    else:                           # v1[] < v2[]
                        i1 += 1
                    if i1 == len(v1) and i2 < len(v2):
                        while i2 < len(v2):
                            v1.append((v2[i2][0], v2[i2][1]))
                            i2 += 1
                index += 1
            v1 = [(item[0], float(item[1])/float((len(cluster)))) for item in v1]  # new centroid - use float
            centroid_list[key] = v1

        # stop iteration judgement: compare old centroid list & current centroid list
        converge = True
        for cur, old in zip(centroid_list, old_centroid_list):
            if (1 - get_dis(cur, old)) > 10e-5:     
                converge = False
                break
        if converge:
            stop = True

    # OUTPUT RES
    for key, cluster in clusters.iteritems():       # key is the cluster index, cluster is a list of vector_index
        for index in cluster:
            print str(index) + " " + str(key)


# the function to generate vector list from string - term frequency
def get_list_tf(v_str):
    v_list = []
    v_arr = v_str.strip().split()
    for item in v_arr:
        item_arr = item.split(":")
        v_list.append(((item_arr[0]), int(item_arr[1])))
    v_list.sort(key=lambda tup: tup[0])     # sort by word , increasing
    return v_list


# the function to calculate the cosine distance between two vectors
def get_dis(v1, v2):
    v1 = normalize(v1)
    v2 = normalize(v2)
    i1 = 0
    i2 = 0
    res = 0.0
    while i1 < len(v1) and i2 < len(v2):
        if v1[i1][0] == v2[i2][0]:
            res += float(v1[i1][1]) * float(v2[i2][1])
            i1 += 1
            i2 += 1
        elif v1[i1][0] > v2[i2][0]:
            i2 += 1
        else:
            i1 += 1
    return res
# the function to normalize vector
def normalize(v):
    leng = 0.0
    for pair in v:
        leng += pair[1] * pair[1]
    leng = float(math.sqrt(leng))
    normalized_v = [(item[0], item[1]/leng) for item in v]
    return normalized_v
if __name__ == '__main__':
    main()