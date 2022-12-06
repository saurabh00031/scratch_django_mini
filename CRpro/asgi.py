"""
ASGI config for CRpro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRpro.settings')

application = get_asgi_application()



#include <bits/stdc++.h>
using namespace std;

int total = 0;
pair<int,int> farthestNode(vector<int> adj[],int s,int isVisited[])
{
    isVisited[s] = 1;
    
    int node = s;
    int dist = 0;
    for(int i = 0;i<adj[s].size();i++)
    {
        int f = adj[s][i];
        
        if(isVisited[f] == 0)
        {
            pair<int,int> temp = farthestNode(adj,f,isVisited);
            
            if(temp.second > dist)
            {
                node = temp.first;
                dist = temp.second;
            }
        }
    }
    return {node,dist + 1};

}
int dfs(vector<int> adj[],int s,int isVisited[])
{
    isVisited[s] = 1;
    int ans = 0;
    for(int i=0;i<adj[s].size();i++)
    {
        int f = adj[s][i];
        
        if(isVisited[f] == 0)
        {
            ans += dfs(adj,f,isVisited);
        }
    }
    total += ans + 1;
    return ans + 1;
}

int maxPoints(vector<vector<int>> &edges)
{
    // Your code goes here
    total = 0;
    int n = edges.size() + 1;
    
    if(n == 1)
    {
        return 1;
    }
    
    vector<int> adj[n+1];
    
    for(int i=0;i<edges.size();i++)
    {
        adj[edges[i][0]].push_back(edges[i][1]);
        adj[edges[i][1]].push_back(edges[i][0]);
    }
    
    int isVisited[n+1];
    
    for(int i=0;i<n+1;i++)
    {
        isVisited[i] = 0;
    }
    
    int farNode = -1;
    int node = -1;
    for(int i=1;i<=n;i++)
    {
        if(adj[i].size() == 1)
        {
            farNode = farthestNode(adj,i,isVisited).first;
            node = i;
            break;
        }
    }
    
    int ans = 1;
    memset(isVisited,0,sizeof(isVisited));
    int temp = dfs(adj,node,isVisited);
    ans = max(ans,total);
    total = 0;
    memset(isVisited,0,sizeof(isVisited));
    temp = dfs(adj,farNode,isVisited);
    ans = max(ans,total);
    
    return ans;
    
}

int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        vector<vector<int>> edges;
        
        for(int i=0;i<n-1;i++)
        {
            int u,v;cin>>u>>v;
            
            vector<int> temp;
            temp.push_back(u);
            temp.push_back(v);
            edges.push_back(temp);
        }
        cout<<maxPoints(edges)<<endl;
    }
    return 0;
}
