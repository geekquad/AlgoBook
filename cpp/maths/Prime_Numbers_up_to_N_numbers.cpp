#include<bits/stdc++.h>
using namespace std;
vector<int>prime;
vector<bool>vis;
void sieve(int n)
{
    for(int i=2;i*i<=n;i++){
        if(vis[i]==false){
            for(int j=i*i;j<=n;j+=i){
                vis[j]=true;
                //All numbers j will be composite
            }
        }
    }
    for(int i=2;i<=n;i++){
        if(!vis[i])
            prime.push_back(i);
        //vis[i]=0 implies that i will be prime
    }
}
//Sieve of Erasthosthenes
int main(){
	int n;
	cout<<"Enter the number N:"<<endl;
	cin>>n;
	vis.assign(n+1,false);
	sieve(n);
	cout<<"Prime numbers upto "<<n<<endl;
	for(auto p:prime){
		cout<<p<<endl;
	}
    //prime is a vector of prime numbers
	return 0;
}