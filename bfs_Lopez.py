import sys
import graph

#takes in a graph and performs a bfs
def BFS(g):
    s = g.nodes[g.head]
    s.discovered = True
    L = [[s.index]]
    i = 0
    T = []

    #algorithm
    while L[i]:
        L.append([])
        for u in L[i]:
            for v in g.nodes[u].children:
                if g.nodes[v].discovered == False:
                    g.nodes[v].discovered = True
                    T.append((u, v))
                    L[i+1].append(v)
        i+=1

    #take the L
    return L


#perform bfs/dfs on a tree
def main():
    #check input
    if(len(sys.argv) < 2):
        print("Usage: python bfs_Lopez.py <graph_n.txt>")
        sys.exit()
    
    #run program
    myGraph = graph.read_file(sys.argv[1])
    search = BFS(myGraph)

    #print output
    for layer in search:
        if layer:
            for item in layer:
                print(str(item)+' ', end = '')

if __name__ == "__main__":
    main()