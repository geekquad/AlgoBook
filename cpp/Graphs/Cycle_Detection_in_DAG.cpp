#include<iostream>
#include<set>
#define NODE 5
using namespace std;

//DIRECTED ACYCLIC GRAPH ( A directed graph with no self cycle)
int graph[NODE][NODE] = {
   {0, 1, 1, 0, 0},
   {0, 0, 0, 0, 0},
   {0, 0, 0, 1, 0},
   {0, 1, 0, 0, 0},
   {0, 1, 0, 1, 0}
};

/*
 1 -> 2 ,3
 3 -> 4
 4 -> 2
 5 -> 2,4
*/

bool dfs(int curr, set<int>&wSet, set<int>&gSet, set<int>&bSet) {
   //moving curr to white set to grey set.
   wSet.erase(wSet.find(curr));
   gSet.insert(curr);

   for(int v = 0; v < NODE; v++) {
      if(graph[curr][v] != 0) {    //for all neighbour vertices
         if(bSet.find(v) != bSet.end())
            continue;    //if the vertices are in the black set
         if(gSet.find(v) != gSet.end())
            return true;    //it is a cycle
         if(dfs(v, wSet, gSet, bSet))
            return true;    //cycle found
      }
   }

   //moving v to grey set to black set.
   gSet.erase(gSet.find(curr));
   bSet.insert(curr);
   return false;
}

bool hasCycle() {
   set<int> wSet, gSet, bSet;    //three set as white, grey and black
   for(int i = 0; i<NODE; i++)
      wSet.insert(i);    //initially add all node into the white set

   while(wSet.size() > 0) {
      for(int current = 0; current < NODE; current++) {
         if(wSet.find(current) != wSet.end())
            if(dfs(current, wSet, gSet, bSet))
               return true;
      }
   }
   return false;
}

int main() {
   bool res;
   res = hasCycle();
   if(res)
      cout << "The graph has cycle." << endl;
   else
      cout << "The graph has no cycle." << endl;
}
