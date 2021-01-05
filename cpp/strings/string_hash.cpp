#include<iostream>
#include<vector>
#include<string>
#include<bitset>
#include<functional>
using namespace std;
// this is to demonstrate the string hashing
void string_hashing(string s)
{
  // instantiating the object
  hash<string> hash_string;
  cout<<"String hash value of the string: "<<hash_string(s)<<"\n";
}
// this function demonstrates vector<bool> hashing
void vector_hashing(string s)
{
  vector<bool> vec{true,false,true,false};
  // instantiating the object
  hash<vector<bool>> hash_vector;
  cout<<"Vector<bool> hash value of the string: "<<hash_vector(vec)<<"\n";
}
// this function demonstrates bitset hashing
void bitset_hashing(string s)
{
  // the bitset is set to 10101
  bitset<5> bit("10101");
  // instantiating the object
  hash<bitset<5>> hash_bitset;

  cout<<"Bitset hashing 10101 value of the string: "<<hash_bitset(bit)<<"\n";
}
int main()
{
  int n;
cout<<"Enter the number of strings you want to enter:"<<"\n";
cin>>n;
string s[n];
cout<<"Enter the strings:"<<"\n";
for(int i=0;i<n;i++)
{
cin>>s[i];
string_hashing(s[i]);
vector_hashing(s[i]);
bitset_hashing(s[i]);
}
  return 0;
}

// Example
// Enter the number of strings you want to enter:
// 3
// Enter the strings:
// string
// String hash value of the string: 41168278
// Vector<bool> hash value of the string: 649440278
// Bitset hashing 10101 value of the string: 2529245748
// string
// String hash value of the string: 41168278
// Vector<bool> hash value of the string: 649440278
// Bitset hashing 10101 value of the string: 2529245748
// hashing
// String hash value of the string: 2495300193
// Vector<bool> hash value of the string: 649440278
// Bitset hashing 10101 value of the string: 2529245748

// When the strings are similar the hash values are also same as seen in the example.
