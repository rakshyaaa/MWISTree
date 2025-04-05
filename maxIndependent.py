def main():
    #Sample Input
    input_data = [
        "11",
        "0 15",
        "1 8",
        "1 16",
        "1 18",
        "2 3",
        "2 5",
        "2 5",
        "3 7",
        "4 2",
        "4 9",
        "6 4",
    ]

    n = int(input_data[0])
    weight = [0] * (n + 1) #store weights in node
    tree = [[] for _ in range(n + 1)] #creating a tree structure

    #building the tree
    for i in range(1, n + 1):
        p, w = map(int, input_data[i].split())
        print(p,w)
        weight[i] = w
        if p != 0:
            tree[p].append(i)
            print(tree)

    dp = [[0, 0] for _ in range(n + 1)]  #each dp[i] = [exclude_weight, include_weight]
    print(dp)

    #DFS Traversal 
    def dfs(u):
        dp[u][1] = weight[u]

        for v in tree[u]: #for every child of u
            dfs(v)
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

    dfs(1) #start exploring the entire tree, calculating dp values at each nodes starting from the bottom all the way up to the root
    print("Maximum-Weight Independent Set:", max(dp[1][0], dp[1][1]))


if __name__ == "__main__":
    main()
