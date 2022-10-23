#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,k,m;
    cin >> n;
    cin >> k;
    int i;
    vector<int> a; 
    for(i = 0; i  < n ;i++){
        cin >> m;
        a.push_back(m);
    }
    priority_queue<int ,vector <int> , greater <>> pq;
    for(i = 0 ; i < k + 1;i++){
        pq.push(a[i]);
    }
    int index = 0;
    for(i = k + 1 ;i < n ; i++){
        a[index++] = pq.top();
        pq.pop();
        pq.push(a[i]);
    }
    while(!pq.empty()){
        a[index++] = pq.top();
        pq.pop();
    }

    for(i = 0 ; i < n ; i++) cout << a[i] << " " ;
    cout << endl;
}
