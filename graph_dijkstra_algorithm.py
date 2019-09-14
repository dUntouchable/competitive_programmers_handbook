#
# Bellman-Ford algorithm - finds shortest paths from a starting node to all nodes of the graph.
#
# here the starting node is 1, and stored in defaultdict, the value to the key is a tuple of
# connected node, and the weight of the edge
#


from collections import defaultdict
from math import inf


def add_edge(ddict, u, v, weights):
    tup = (v,weights)
    ddict[u].append(tup)

def print_graph(adlist):
    for k,v in adlist.items():
        print(k,"->",v)

adlist = defaultdict(list)

add_edge(adlist, 1, 2, 5)
add_edge(adlist, 1, 4, 7)
add_edge(adlist, 1, 3, 3)
add_edge(adlist, 2, 4, 3)
add_edge(adlist, 2, 6, 2)
add_edge(adlist, 3, 4, 1)
add_edge(adlist, 4, 6, 2)
add_edge(adlist, 6, None, None)

print_graph(adlist)

distance = [inf] * (max(adlist.keys()) + 1)
distance[1] = 0
print(distance)

for key in adlist.keys():
    for tup in adlist[key]:
        if tup[0] is not None or tup[1] is not None:
            distance[tup[0]] = min(distance[tup[0]], distance[key] + tup[1])
print("\nDistance from node 1 are :")
for key in adlist.keys():
    print("1 -> ", key, " is ",distance[key])
