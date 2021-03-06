from graph import *


g1 = Graph()
g1.add(12, edgeType=0)
g1.add(4, [0], edgeType=1)
g1.add(8, [14, 4], edgeType=1)
g1.add(14, [13,0], edgeType=1)
g1.add(13, [0], edgeType=1)
g1.add(0, [8], edgeType=1)
g1.add(7, [6,11], edgeType=0)
g1.add(6, [7,11], edgeType=0)
g1.add(11, [7,6], edgeType=0)
g1.add(5, [17,16], edgeType=1)
g1.add(1, [5], edgeType=1)
g1.add(3,[9], edgeType=0)
g1.add(9,[15, 2], edgeType=0)
g1.add(2,[15], edgeType=0)
g1.add(15,[10], edgeType=0)
g1.description = "A graph with directed and undirected edges with no weights on any edge"
# print(g1.graph)


# ___________________________________________________
g2 = Graph()
g2.add("a", ["b", "c"], [1, 4])
g2.add("b", ["d", "c"], [5, 1])
g2.add("c", ["d", "b"], [3, 1])
g2.add("d", ["e", "g", "f"], [8, 9, 3])
g2.add("e", ["g"], [2])
g2.add("f", ["g"], [5])
g2.description = "A graph with undirected edges with weights on edges"
# print(g2.graph)

# ________________________same g2 graph as g3
g3  = Graph()
g3.addFromDict("a", {"b":1,"c":4})
g3.addFromDict("b", {"d":5,"c":1})
g3.addFromDict("c", {"d":3,"b":1})
g3.addFromDict("d", {"e":8,"g":9, "f":3})
g3.addFromDict("e", {"g":2})
g3.addFromDict("f", {"g":5})
g3.description = "A graph with undirected edges with weights on edges"
# print(g3.graph)

# ____________________________________________________
g4 = Graph()
g4.addFromDict("s", {"a":3,"b":5}, edgeType=1)
g4.addFromDict("a", {"d":3,"b":4}, edgeType=1)
g4.addFromDict("b", {"c":4}, edgeType=1)
g4.addFromDict("d", {"g":5}, edgeType=1)
g4.addFromDict("c", {"e":6}, edgeType=1)
g4.description = "A DAG with weights on edges"
# print(g4)

# ____________________________________________________
g5 = Graph()
g5.addFromDict("a", {"b":4, "d":5})
g5.addFromDict("b", {"c":4, "e":5})
g5.addFromDict("d", {"a":5, "e":2})
g5.addFromDict("e", {"b":5, "f":4, "d":2})
g5.addFromDict("f", {"g":3})
g5.addFromDict("s", {"a":3, "d":4})
g5.description = "A graph with undirected edges with weights on edges"
# print(g5)

# _____________________________________________________
g6 = Graph()
g6.add("a", ['d'], edgeType=1)
g6.add("d", ['h', 'g'], edgeType=1)
g6.add("h", ['j', 'i'], edgeType=1)
g6.add("g", ['i'], edgeType=1)
g6.add("i", ['l'], edgeType=1)
g6.add("j", ['i', 'm'], edgeType=1)
g6.add("j", ['i', 'm'], edgeType=1)
g6.add("c", ['a', 'b'], edgeType=1)
g6.add("b", ['d'], edgeType=1)
g6.add("e", ['d', 'a', 'f'], edgeType=1)
g6.add("f", ['j', 'k'], edgeType=1)
g6.add("f", ['j', 'k'], edgeType=1)
g6.add("k", ['j'], edgeType=1)
g6.description = "A DAG with no weights on any edge"

# ___________________________________________________
g7 = Graph()
g7.addFromDict("a", {"b":3, "c":6}, edgeType=1)
g7.addFromDict("b", {"e":11, "c":4, "d":4}, edgeType=1)
g7.addFromDict("c", {"g":11, "d":8}, edgeType=1)
g7.addFromDict("d", {"g":2, "e":-4, "f":5}, edgeType=1)
g7.addFromDict("e", {'h':9}, edgeType=1)
g7.addFromDict("f", {'h':1}, edgeType=1)
g7.addFromDict("g", {'h':2}, edgeType=1)
g7.description = "A DAG with weights (-ve or +ve) on every edge"

# _______________________________________________________________
g8 = Graph()
g8.addFromDict(0, {1:4, 2:1}, edgeType=1)
g8.addFromDict(1, {3:1}, edgeType=1)
g8.addFromDict(2, {1:2, 3:5}, edgeType=1)
g8.addFromDict(3, {4:3}, edgeType=1)
g8.description = "a directed graph with positive wights on each edge"

# __________________________________________________________________
g9 = Graph()
g9.addFromDict(0, {1:5, 2:1}, edgeType=1)
g9.addFromDict(1, {4:20, 3:3, 2:2}, edgeType=1)
g9.addFromDict(2, {4:12, 1:3}, edgeType=1)
g9.addFromDict(3, {4:2, 2:3, 5:6}, edgeType=1)
g9.addFromDict(4, {5:1}, edgeType=1)
g9.description = "a directed graph with positive wights on each edge"

# __________________________________________________________________
g10 = Graph()
g10.addFromDict(0, {1:4, 6:2})
g10.addFromDict(6, {4:2})
g10.addFromDict(1, {1:-1, 2:3})
g10.addFromDict(2, {4:1, 3:3})
g10.addFromDict(4, {5:2})
g10.addFromDict(3, {5:-2})
g10.description = "a directed graph with negative cycle"

# __________________________________________________________________
g11 = Graph()
g11.addFromDict(0, {1:5}, edgeType=1)
g11.addFromDict(3, {2:-15}, edgeType=1)
g11.addFromDict(6, {7:-50}, edgeType=1)
g11.addFromDict(1, {6:60, 5:30, 2:20}, edgeType=1)
g11.addFromDict(2, {4:75, 3:10}, edgeType=1)
g11.addFromDict(7, {8:-10}, edgeType=1)
g11.addFromDict(5, {6:5, 8:50, 4:25}, edgeType=1)
g11.addFromDict(4, {9:100}, edgeType=1)
g11.description = "a directed graph with negative cycle"

# ____________________________________________________________________
g12 = Graph()
g12.add(0, [1], edgeType=1)
g12.add(1, [2], edgeType=1)
g12.add(2, [0], edgeType=1)
g12.add(3, [4,7], edgeType=1)
g12.add(4, [5], edgeType=1)
g12.add(5, [0,6], edgeType=1)
g12.add(6, [2,0,4], edgeType=1)
g12.add(7, [5,3], edgeType=1)
g12.description = "a directed graph with cycles"

# ____________________________________________________________________
g13 = Graph()
g13.add(0, [1], edgeType=1)
g13.add(1, [2,3,4], edgeType=1)
g13.add(2, [0,4], edgeType=1)
g13.add(3, [5], edgeType=1)
g13.add(4, [5], edgeType=0)
g13.description = "a directed graph with cycles"

# ____________________________________________________________________
g14 = Graph()
g14.add(0, [1, 2])
g14.add(1, [0, 2])
g14.add(2, [0, 1, 3, 5])
g14.add(3, [2, 4])
g14.add(5, [2, 8, 6])
g14.add(6, [5, 7])
g14.add(7, [6, 8])
g14.add(8, [5, 7])
g14.description = "undirected graph with many cycles and bridges"

# _____________________________________________________________________
G=Graph()
G.add(3, [2])
G.add(2, [0,4])
G.add(0, [6,5])
G.add(4, [5,1])
G.description = "undirected un-weighted simple graph"