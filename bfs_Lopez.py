import sys
import graph

def BFS(s):
    'bfs'

#perform bfs/dfs on a tree
def main():
    if(len(sys.argv) < 2):
        print("Usage: python bfs_Lopez.py <graph_n.txt>")
        sys.exit()
    
    myGraph = graph.read_file(sys.argv[1])

if __name__ == "__main__":
    main()