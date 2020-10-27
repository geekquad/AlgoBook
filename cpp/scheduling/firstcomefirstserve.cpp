#include <iostream>
using namespace std;

void findwt(int processes[] , int n, int bt[], int wt[]){
    wt[0] = 0;
    for(int i = 1; i < n ; i++){
        wt[i] = wt[i-1] + bt[i-1];
    }
}
void findtat(int processes[], int n, int bt[], int wt[], int tat[]){
    for(int i = 0; i < n ; i++){
        tat[i] = wt[i] + bt[i];
    }
}
void findavgtime(int processes[], int n, int bt[]){
    int total_tat, total_wt = 0;
    int wt[n];
    int tat[n];

    findwt(processes,n,bt,wt);
    findtat(processes,n,bt,wt,tat);

    for(int i = 0; i < n; i++){
        total_tat = total_tat + tat[i];
        total_wt = total_wt + wt[i];
    }

    cout << "Avg wt = " << (float)total_wt / n << endl;
    cout << "Avg tat = " << (float)total_tat / n << endl;
}

int main(){

    int processes[] = {1,2,3};
    int bt[] = {10,5,8};

    findavgtime(processes, 3, bt);

    return 0;
}
