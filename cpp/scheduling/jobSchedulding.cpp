#include <iostream>
#include<vector>
#include<algorithm>
#define ll long long int
using namespace std;

struct job{
    char id;
    int deadline;
    int profit;
};

bool cmp(job a, job b) 
{
    """ comparator function for sorting jobs by their profit in decreasing order """ 
    return (a.profit > b.profit); 
}

int maxDeadline(vector<job> &jobSequence)
{
    """ calculates max deadline """
    int max = -1;
    for(int i = 0; i < jobSequence.size(); i++)
    {
        if(jobSequence[i].deadline > max)
        {
            max = jobSequence[i].deadline;
        }
    }
    
    return max;
}

int main() {
    
    int n;
    cout << "Enter the number of jobs : ";
    cin >> n;
    
    vector <job> jobSequence(n);
    cout << "Enter id , deadline , profit for each job : \n";
    for(int i = 0; i < n; i++)
    {
        job j;
        cin >> j.id >> j.deadline >> j.profit ;
        jobSequence[i] = j;
        
        cout << jobSequence[i].id << jobSequence[i].deadline << "\n";
        
        
    }
    
    sort(jobSequence.begin() , jobSequence.end() , cmp);
    
    int m = maxDeadline(jobSequence);
    vector<int> availableDeadlines(m , 1);
    vector<char> sequenceId;
    
    ll totalProfit = 0;
    
    
    for(int i = 0; i < n; i++)
    {
        
        int deadlineLimit = jobSequence[i].deadline;

        // For each job , find the highest deadline to which it can be assigned
        for(int j = deadlineLimit - 1; j >= 0; j--)
        {
            if(availableDeadlines[j] == 1)
            {
                
                availableDeadlines[j] = 0;
                totalProfit += jobSequence[i].profit;
                sequenceId.push_back(jobSequence[i].id);
                break;
                
            }
        }
    }
    
    
    cout << "The total profit is : " << totalProfit << "\n";
    
    cout << "The sequence oj jobs : ";
    for(int i = 0; i < sequenceId.size(); i++)
    {
        cout << sequenceId[i] << " ";
    }
     cout << "\n";
    
    
    

	return 0;
}
