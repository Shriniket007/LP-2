#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[])
    {
        int vis[V] = {0};
        vis[0] = 1;
        queue<int> q;
        // push the initial starting node
        q.push(0);
        vector<int> bfs;
        // iterate till the queue is empty
        while (!q.empty())
        {
            // get the topmost element in the queue
            int node = q.front();
            q.pop();
            bfs.push_back(node);
            // traverse for all its neighbours
            for (auto it : adj[node])
            {
                // if the neighbour has previously not been visited,
                // store in Q and mark as visited
                if (!vis[it])
                {
                    vis[it] = 1;
                    q.push(it);
                }
            }
        }
        return bfs;
    }
};

void addEdge(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void printAns(vector<int> &ans)
{
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }
}

int main()
{
    // vector<int> adj[6];
    int n;
    cout << "Enter the number of nodes:";
    cin >> n;
    vector<int> adj[n];

    int e;
    cout << "Enter the number of edges:";
    cin >> e;

    for (int i = 0; i < e; i++)
    {
        int start, end;
        cout << "Enter the start node:";
        cin >> start;
        cout << "Enter the end node:";
        cin >> end;
        addEdge(adj, start, end);
    }

    // addEdge(adj, 0, 1);
    // addEdge(adj, 1, 2);
    // addEdge(adj, 1, 3);
    // addEdge(adj, 0, 4);

    Solution obj;
    vector<int> ans = obj.bfsOfGraph(n, adj);
    printAns(ans);

    return 0;
}