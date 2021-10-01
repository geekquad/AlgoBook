// C++ Program for Floyd Warshall Algorithm  
#include <bits/stdc++.h> 
using namespace std;  
#define w 4  
#define INF 999999 
void print(int distance[][w])  
{  
    for (int i = 0; i < w; i++)  
    {  
        for (int j = 0; j < w; j++)  
        {  
            if (distance[i][j] == INF)  
                cout<<"INF"<<"   ";  
            else
                cout<<distance[i][j]<<"     ";  
        }  
        cout<<endl;  
    }  
}     
void floydWarshall (int graph[][w])  
{  
    
    int distance[w][w], i, j, l;  
    for (i = 0; i < w; i++)  
        for (j = 0; j < w; j++)  
            distance[i][j] = graph[i][j];  
    for (l = 0; l < w; l++)  
    {  
        for (i = 0; i < w; i++)  
        {  
            for (j = 0; j < w; j++)  
            {   
                if (distance[i][l] + distance[l][j] < distance[i][j])  
                    distance[i][j] = distance[i][l] + distance[l][j];  
            }  
        }  
    }  
    print(distance);  
}   
// Driver code  
int main()  
{  
    /* weighted graph  
         10  
    (0)------->(3)  
    |          /|\  
   5|           |  
    |           | 1  
    \|/         |  
    (1)------->(2)  
          3     */
    int graph[w][w] = { {0, 5, INF, 10},  
                        {INF, 0, 3, INF},  
                        {INF, INF, 0, 1},  
                        {INF, INF, INF, 0}  
                    };    
    floydWarshall(graph);  
    return 0;  
} 