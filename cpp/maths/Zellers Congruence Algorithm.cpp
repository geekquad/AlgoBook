#include<bits/stdc++.h>

using namespace std;

int Zellercongruence(int day, int month, int year)
{
    if (month<3)
    {
        month += 12;
        year--;
    }
   int q = day;
   int m = month;
   int k = year % 100;
   int j = year / 100;
   int h = q + 13*(m+1)/5 + k + k/4 + j/4 + 5*j;
   h = h % 7;
   switch (h)
   {
       case 0 : cout << "Saturday \n"; break;
       case 1 : cout << "Sunday \n"; break;
       case 2 : cout << "Monday \n"; break;
       case 3 : cout << "Tuesday \n"; break;
       case 4 : cout << "Wednesday \n"; break;
       case 5 : cout << "Thursday \n"; break;
       case 6 : cout << "Friday \n"; break;
   }
   return 0;
}

int main()
{
    char d;
    int day,month,year;
    cout<<"Enter date in DD/MM/YYYY format: ";
    cin>>day>>d>>month>>d>>year;
    Zellercongruence(day,month,year); //date (dd/mm/yyyy)
    return 0;
}
