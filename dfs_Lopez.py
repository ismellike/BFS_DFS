import sys
import graph

#takes in a graph and performs a dfs
def DFS(g):
    s = g.nodes[g.head]
    stack = [s]
    L = []

    #algorithm
    while stack:
        u = stack.pop(0)
        if u.discovered == False:
            u.discovered = True
            L.append(u.index)
            u.children.reverse()
            for v in u.children:
                stack.insert(0, g.nodes[v])

    #take the L
    return L

#perform bfs/dfs on a tree
def main():
    #check input
    if(len(sys.argv) < 2):
        print("Usage: python dfs_Lopez.py <graph_n.txt>")
        sys.exit()
    
    #run program
    myGraph = graph.read_file(sys.argv[1])
    search = DFS(myGraph)

    #print output
    print(' '.join(map(str, search)))

if __name__ == "__main__":
    main()