#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
void createLPS(string pattern,ll m,ll *lps)
{
    ll len=0; //length of the previous longest prefix which is also a suffix 
    lps[0]=0;
    ll i=1;
    while(i<m)
    {
        if(pattern[i]==pattern[len])
        {
            len++;
            lps[i]=len;
            i++;
        }
        else
        {
            if(len!=0)
            {
                len=lps[len - 1]; 
            }
            else
            {
                lps[i]=0;
                i++;
            }
        }
    }
}
void KMP(string pattern,string text,ll n,ll m)
{
    ll i=0,j=0;
    ll lps[m];
    createLPS(pattern,m,lps);
    while(i<n)
    {
        if(pattern[j]==text[i])
        {
            i++;
            j++;
        }
        if(j==m)
        {
            cout<<"Pattern is found at index :"<<i-j<<endl;
            j=lps[j-1];
        }
        else
        if(i<n && pattern[j]!=text[i])
        {
            if(j!=0)
            j=lps[j-1];
            else
            i++;
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string text,pattern;
    cin>>text>>pattern;
    //input a string with spaces 
    /*getline(cin,text);
    getline(cin,pattern);*/
    ll n=text.length();
    ll m=pattern.length();
    KMP(pattern,text,n,m);
    return 0;
}
