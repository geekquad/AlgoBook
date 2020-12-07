#include<bits/stdc++.h>

using namespace std;
void createZarray(string str, int Z[]){
   int n = str.length();
   int L, R, k;
   L = R = 0;
   for (int i = 1; i < n; ++i){
      if (i > R){
         L = R = i;
         while (R<n && str[R-L] == str[R])
         R++;
         Z[i] = R-L;
         R--;
      } else {
         k = i-L;
         if (Z[k] < R-i+1)
            Z[i] = Z[k];
         else {
            L = i;
            while (R<n && str[R-L] == str[R])
               R++;
            Z[i] = R-L;
            R--;
         }
      }
   }
}
void zAlgorithm(string text, string pattern){
   string str = pattern+"$"+text;
   int len = str.length();
   int Z[len];
   createZarray(str, Z);
   for (int i = 0; i < len; ++i){
      if (Z[i] == pattern.length())
         cout<<(i-pattern.length()-1)<<", ";
   }
}
int main(){
   string str,pattern;
   cout<<"Enter the string:";
   getline(cin,str);
   cout<<"Enter the pattern:";
   getline(cin,pattern);
   cout<<"The patter ' "<<pattern<<" ' is found in the string '"<<str<<" ' at index ";
   zAlgorithm(str, pattern);
   return 0;
}

