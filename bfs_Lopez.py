import sys
import graph

#pass the head
def BFS(g):
    s = g.nodes[g.head]
    s.discovered = True
    L = [[s.index]]
    i = 0
    T = []

    while L[i]:
        L.append([])
        for u in L[i]:
            for v in g.nodes[u].children:
                if g.nodes[v].discovered == False:
                    g.nodes[v].discovered = True
                    T.append((u, v))
                    L[i+1].append(v)
        i+=1
    return L


#perform bfs/dfs on a tree
def main():
    if(len(sys.argv) < 2):
        print("Usage: python bfs_Lopez.py <graph_n.txt>")
        sys.exit()
    
    myGraph = graph.read_file(sys.argv[1])
    search = BFS(myGraph)
    print(bfs)

if __name__ == "__main__":
    main()