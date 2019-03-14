import sys
import graph

#pass the head
def BFS(s):
    s.discovered = True

#perform bfs/dfs on a tree
def main():
    if(len(sys.argv) < 2):
        print("Usage: python bfs_Lopez.py <graph_n.txt>")
        sys.exit()
    
    head = graph.read_file(sys.argv[1])
    BFS(head)


if __name__ == "__main__":
    main()