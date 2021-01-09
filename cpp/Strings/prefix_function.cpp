/*****
 * prefix_function.cpp
 * 
 * Created by: Jordan Van Leeuwen
 * 
 * Date: 1/7/2021
*****/

#include <vector>
#include <string>
//#include <iostream> (include this when testing)

/******
 * creates a prefix table for the KMP string search algorithm
 * 
 * args: a string of the pattern being searched for
 * 
 * return: vector of the prefix table 
 *****/
std::vector<unsigned int> prefixFunction(std::string pattern)
{
	std::vector<unsigned int> prefixTable(pattern.size());	// prefix table

	unsigned int j = 0;	// value to be inserted into the prefix table

	// for each element of the pattern string except for the first...
	for (unsigned int i = 1; i < pattern.size(); i++)
	{
		// each time the element at j does not match the element at i...
		while (j > 0 && pattern[j] != pattern[i])
			j = prefixTable[j - 1];

		// if the element at j matches the element at i...
		if (pattern[j] == pattern[i])
			j++;

		// insert the value into the prefix table
		prefixTable[i] = j;
	}
	return prefixTable;
}

// the method found below can be used to test the prefix function algorithm

/*
int main()
{
	std::string p;

	std::vector<unsigned int> table;

	std::cin >> p;

	table = prefixFunction(p);

	for (unsigned int i = 0; i < table.size(); i++)
	{
		std::cout << table[i] << std::endl;
	}

	return 0;
}
*/