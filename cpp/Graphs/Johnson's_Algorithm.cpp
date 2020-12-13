#include<iostream>
#define INF 9999
using namespace std;
int min(int a, int b);
int cost[10][10], adj[10][10];
inline int min(int a, int b){
   return (a<b)?a:b;
}
main() {
   int vert, edge, i, j, k, c;
   cout << "Enter no of vertices: ";
   cin >> vert;
   cout << "Enter no of edges: ";
   cin >> edge;
   cout << "Enter the EDGE Costs:\n";
   for (k = 1; k <= edge; k++) { 
      cin >> i >> j >> c;
      adj[i][j] = cost[i][j] = c;
   }
   for (i = 1; i <= vert; i++)
      for (j = 1; j <= vert; j++) {
         if (adj[i][j] == 0 && i != j)
            adj[i][j] = INF; //if there is no edge, put infinity
      }
   for (k = 1; k <= vert; k++)
      for (i = 1; i <= vert; i++)
         for (j = 1; j <= vert; j++)
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]); 
   cout << "Resultant adj matrix\n";
   for (i = 1; i <= vert; i++) {
      for (j = 1; j <= vert; j++) {
            if (adj[i][j] != INF)
               cout << adj[i][j] << " ";
      }
      cout << "\n";
   }
}
/* Example input and output
Enter no of vertices: 3
Enter no of edges: 5
Enter the EDGE Cost:
1 2 4
2 1 6
1 3 11
3 1 3
2 3 2
Resultant adj matrix
0 4 6 
5 0 2 
3 7 0 
*/


